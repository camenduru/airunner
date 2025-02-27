import functools
import os
import torch
from airunner.aihandler.settings import LOG_LEVEL
from airunner.aihandler.logger import Logger as logger
import logging
from dataclasses import dataclass
logging.disable(LOG_LEVEL)
logger.set_level(logger.DEBUG)



@dataclass
class UNet2DConditionOutput:
    sample: torch.FloatTensor


class TracedUNet(torch.nn.Module):
    def __init__(self, pipe):
        super().__init__()
        self.config = pipe.unet.config
        self.in_channels = pipe.unet.in_channels
        self.device = pipe.unet.device

    def forward(self, latent_model_input, t, encoder_hidden_states, **kwargs):
        unet_traced = torch.jit.load("unet_traced.pt")
        sample = unet_traced(latent_model_input, t, encoder_hidden_states)[0]
        return UNet2DConditionOutput(sample=sample)
            


class MemoryEfficientMixin:
    torch_compile_applied: bool = False

    last_channels_applied: bool = None
    vae_slicing_applied: bool = None
    attention_slicing_applied: bool = None
    tiled_vae_applied: bool = None
    accelerated_transformers_applied: bool = None
    cpu_offload_applied: bool = None
    model_cpu_offload_applied: bool = None

    def reset_applied_memory_settings(self):
        self.last_channels_applied = None
        self.vae_slicing_applied = None
        self.attention_slicing_applied = None
        self.tiled_vae_applied = None
        self.accelerated_transformers_applied = None
        self.cpu_offload_applied = None
        self.model_cpu_offload_applied = None

    def apply_last_channels(self):
        if self.use_kandinsky or self.is_txt2vid or self.is_shapegif:
            return

        if self.last_channels_applied == self.use_last_channels:
            return

        self.last_channels_applied = self.use_last_channels
        if self.use_last_channels:
            logger.info("Enabling torch.channels_last")
            self.pipe.unet.to(memory_format=torch.channels_last)
        else:
            logger.info("Disabling torch.channels_last")
            self.pipe.unet.to(memory_format=torch.contiguous_format)

    def apply_vae_slicing(self):
        if self.vae_slicing_applied == self.use_enable_vae_slicing:
            return
        self.vae_slicing_applied = self.use_enable_vae_slicing

        if self.action not in [
            "img2img", "depth2img", "pix2pix", "outpaint", "superresolution", "controlnet", "upscale"
        ] and not self.use_kandinsky:
            if self.use_enable_vae_slicing or self.is_txt2vid:
                logger.info("Enabling vae slicing")
                try:
                    self.pipe.enable_vae_slicing()
                except AttributeError:
                    pass
            else:
                logger.info("Disabling vae slicing")
                try:
                    self.pipe.disable_vae_slicing()
                except AttributeError:
                    pass

    def apply_attention_slicing(self):
        if self.attention_slicing_applied == self.use_attention_slicing:
            return
        self.attention_slicing_applied = self.use_attention_slicing

        if self.use_attention_slicing:
            logger.info("Enabling attention slicing")
            self.pipe.enable_attention_slicing(1)
        else:
            logger.info("Disabling attention slicing")
            self.pipe.disable_attention_slicing()

    def apply_tiled_vae(self):
        if self.tiled_vae_applied == self.use_tiled_vae:
            return
        self.tiled_vae_applied = self.use_tiled_vae

        if self.use_tiled_vae:
            logger.info("Applying tiled vae")
            # from diffusers import UniPCMultistepScheduler
            # self.pipe.scheduler = UniPCMultistepScheduler.from_config(self.pipe.scheduler.config)
            try:
                self.pipe.vae.enable_tiling()
            except AttributeError:
                logger.warning("Tiled vae not supported for this model")

    def apply_accelerated_transformers(self):
        if self.accelerated_transformers_applied == self.use_accelerated_transformers:
            return
        self.accelerated_transformers_applied = self.use_accelerated_transformers

        from diffusers.models.attention_processor import AttnProcessor, AttnProcessor2_0
        if self.use_kandinsky:
            return
        if not self.cuda_is_available or not self.use_accelerated_transformers:
            logger.info("Disabling accelerated transformers")
            self.pipe.unet.set_attn_processor(AttnProcessor())
        else:
            self.pipe.unet.set_attn_processor(AttnProcessor2_0())

    def save_unet(self, file_path, file_name):
        logger.info(f"Saving compiled torch model {file_name}")
        unet_file = os.path.join(file_path, file_name)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        torch.save(self.pipe.unet.state_dict(), unet_file)

    def load_unet(self, file_path, file_name):
        logger.info(f"Loading compiled torch model {file_name}")
        unet_file = os.path.join(file_path, file_name)
        self.pipe.unet.state_dict = torch.load(unet_file, map_location="cuda")

    def apply_torch_compile(self):
        """
        Torch compile has limited support
            - No support for Windows
            - Fails with the compiled version of AI Runner
        Because of this, we are disabling it until a better solution is found.
        """
        if not self.use_torch_compile or self.torch_compile_applied:
            return
        # unet_path = self.unet_model_path
        # if unet_path is None or unet_path == "":
        #     unet_path = os.path.join(self.model_base_path, "compiled_unet")
        # file_path = os.path.join(os.path.join(unet_path, self.model_path))
        model_name = self.options.get(f"model", None)
        # file_name = f"{model_name}.pt"
        # if os.path.exists(os.path.join(file_path, file_name)):
        #     self.load_unet(file_path, file_name)
        #     self.pipe.unet.to(memory_format=torch.channels_last)
        # else:
        logger.info(f"Compiling torch model {model_name}")
        #self.pipe.unet.to(memory_format=torch.channels_last)
        self.pipe.unet = torch.compile(self.pipe.unet, mode="reduce-overhead", fullgraph=True)
        self.pipe(prompt=self.prompt)
        # self.save_unet(file_path, file_name)
        self.torch_compile_applied = True
    
    def apply_torch_trace(self):
        self.pipe.unet = TracedUNet(self.pipe)

    
    def save_torch_trace(self):
        torch.set_grad_enabled(False)
        unet = self.pipe.unet
        unet.eval()
        unet.to(memory_format=torch.channels_last)  # use channels_last memory format
        unet.forward = functools.partial(unet.forward, return_dict=False)

        def generate_inputs():
            sample = torch.randn(2, 4, 64, 64).half().cuda()
            timestep = torch.rand(1).half().cuda() * 999
            encoder_hidden_states = torch.randn(2, 77, 768).half().cuda()
            return sample, timestep, encoder_hidden_states

        # warmup
        for _ in range(3):
            with torch.inference_mode():
                inputs = generate_inputs()
                orig_output = unet(*inputs)
        
        # trace
        print("tracing..")
        unet_traced = torch.jit.trace(unet, inputs)
        unet_traced.eval()
        print("done tracing")
        unet_traced.save("unet_traced.pt")

    def enable_memory_chunking(self):
        # if self.is_txt2vid:
        #     self.pipe.unet.enable_forward_chunking(chunk_size=1, dim=1)
        return

    def move_pipe_to_cuda(self, pipe):
        if not self.use_enable_sequential_cpu_offload and not self.enable_model_cpu_offload and pipe.device != "cuda":
            logger.info("Moving to cuda")
            pipe.to("cuda") if self.cuda_is_available else None
        return pipe

    def move_pipe_to_cpu(self, pipe):
        logger.info("Moving to cpu")
        try:
            pipe.to("cpu", self.data_type)
        except NotImplementedError:
            logger.warning("Not implemented error when moving to cpu")
        return pipe

    def apply_cpu_offload(self):
        if self.cpu_offload_applied == self.enable_model_cpu_offload:
            return
        self.cpu_offload_applied = self.enable_model_cpu_offload

        if self.use_enable_sequential_cpu_offload and not self.enable_model_cpu_offload:
            logger.info("Enabling sequential cpu offload")
            self.pipe = self.move_pipe_to_cpu(self.pipe)
            try:
                self.pipe.enable_sequential_cpu_offload()
            except NotImplementedError:
                logger.warning("Not implemented error when applying sequential cpu offload")
                self.pipe = self.move_pipe_to_cuda(self.pipe)

    def apply_model_offload(self):
        if self.model_cpu_offload_applied == self.enable_model_cpu_offload:
            return
        self.model_cpu_offload_applied = self.enable_model_cpu_offload

        if self.enable_model_cpu_offload \
           and not self.use_enable_sequential_cpu_offload \
           and hasattr(self.pipe, "enable_model_cpu_offload"):
            logger.info("Enabling model cpu offload")
            self.pipe = self.move_pipe_to_cpu(self.pipe)
            self.pipe.enable_model_cpu_offload()

    def apply_memory_efficient_settings(self):
        logger.info("Applying memory efficient settings")
        self.apply_last_channels()
        self.enable_memory_chunking()
        self.apply_vae_slicing()
        self.apply_cpu_offload()
        self.apply_model_offload()
        self.pipe = self.move_pipe_to_cuda(self.pipe)
        self.apply_attention_slicing()
        self.apply_tiled_vae()
        self.apply_accelerated_transformers()
        #self.apply_torch_compile()
        #self.apply_torch_trace()
