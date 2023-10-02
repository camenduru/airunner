import random

from PIL import Image
from PyQt6.QtCore import pyqtSignal, QRect

from airunner.aihandler.enums import MessageCode
from airunner.aihandler.settings import MAX_SEED
from airunner.data.models import ActionScheduler
from airunner.utils import get_session
from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.generator_form.templates.generatorform_ui import Ui_generator_form
from airunner.widgets.slider.slider_widget import SliderWidget


class GeneratorForm(BaseWidget):
    widget_class_ = Ui_generator_form
    changed_signal = pyqtSignal(str, object)
    deterministic_generation_window = None
    deterministic_images = []
    deterministic_data = None
    deterministic = False
    seed_override = None
    deterministic_index = 0
    requested_image = None
    deterministic_seed = None
    initialized = False
    parent = None

    @property
    def is_txt2img(self):
        return self.generator_section == "txt2img"

    @property
    def is_outpaint(self):
        return self.generator_section == "outpaint"

    @property
    def is_depth2img(self):
        return self.generator_section == "depth2img"

    @property
    def is_pix2pix(self):
        return self.generator_section == "pix2pix"

    @property
    def is_upscale(self):
        return self.generator_section == "upscale"

    @property
    def is_superresolution(self):
        return self.generator_section == "superresolution"

    @property
    def is_txt2vid(self):
        return self.generator_section == "txt2vid"

    @property
    def generator_section(self):
        try:
            return self.property("generator_section")
        except Exception as e:
            print(e)
            return None

    @property
    def generator_name(self):
        try:
            return self.property("generator_name")
        except Exception as e:
            print(e)
            return None

    @property
    def generator_settings(self):
        return self.settings_manager.find_generator(
            self.generator_section,
            self.generator_name
        )

    @property
    def steps(self):
        return self.ui.steps_widget.current_value

    @property
    def ddim_eta(self):
        return self.ui.ddim_eta_widget.current_value

    @property
    def samples(self):
        return self.ui.samples_widget.current_value

    @property
    def model(self):
        return self.ui.model.currentText()

    @property
    def scheduler(self):
        return self.ui.scheduler.currentText()

    @property
    def scale(self):
        return self.ui.scale_widget.current_value

    @property
    def strength(self):
        return self.ui.strength_widget.current_value

    @property
    def random_seed(self):
        return self.settings_manager.generator.random_seed

    @property
    def random_latents_seed(self):
        return self.settings_manager.generator.random_latents_seed

    @property
    def latents_seed(self):
        return self.settings_manager.generator.latents_seed

    @latents_seed.setter
    def latents_seed(self, val):
        self.settings_manager.set_value("generator.latents_seed", val)

    @property
    def seed(self):
        return self.settings_manager.generator.seed

    @seed.setter
    def seed(self, val):
        self.settings_manager.set_value("generator.seed", val)

    @property
    def image_scale(self):
        return self.settings_manager.generator.image_guidance_scale

    @property
    def active_rect(self):
        rect = QRect(
            self.canvas.active_grid_area_rect.x(),
            self.canvas.active_grid_area_rect.y(),
            self.canvas.active_grid_area_rect.width(),
            self.canvas.active_grid_area_rect.height(),
        )
        rect.translate(-self.canvas.pos_x, -self.canvas.pos_y)

        return rect

    @property
    def enable_controlnet(self):
        return self.settings_manager.generator.enable_controlnet

    @property
    def controlnet(self):
        return self.settings_manager.generator.controlnet

    @property
    def controlnet_image(self):
        return self.ui.controlnet_settings.current_controlnet_input_image

    def update_image_input_thumbnail(self):
        self.ui.input_image_widget.set_thumbnail()

    def update_controlnet_settings_thumbnail(self):
        self.ui.controlnet_settings.set_thumbnail()

    """
    Slot functions

    The following functions are defined in and connected to the appropriate
    signals in the corresponding ui file.
    """
    def handle_prompt_changed(self):
        if not self.initialized:
            return
        self.settings_manager.set_value("generator.prompt", self.ui.prompt.toPlainText())

    def handle_negative_prompt_changed(self):
        if not self.initialized:
            return
        self.settings_manager.set_value("generator.negative_prompt", self.ui.negative_prompt.toPlainText())

    def toggle_prompt_builder_checkbox(self, toggled):
        pass

    def handle_model_changed(self, name):
        if not self.initialized:
            return
        self.settings_manager.set_value("generator.model", name)
        self.changed_signal.emit("generator.model", name)

    def handle_scheduler_changed(self, name):
        if not self.initialized:
            return
        self.settings_manager.set_value("generator.scheduler", name)
        self.changed_signal.emit("generator.scheduler", name)

    def toggle_variation(self, toggled):
        pass

    def handle_generate_button_clicked(self):
        self.generate()

    def handle_interrupt_button_clicked(self):
        self.app.client.cancel()
    """
    End Slot functions
    """

    def generate(self, image=None, seed=None):
        if seed is None:
            seed = self.ui.seed_widget.seed
        if self.ui.samples_widget.current_value > 1:
            self.app.client.do_process_queue = False
        total_samples = self.ui.samples_widget.current_value if not self.is_txt2vid else 1
        for n in range(total_samples):
            if self.settings_manager.generator.use_prompt_builder and n > 0:
                seed = int(seed) + n
            self.call_generate(image, seed=seed)
        self.seed_override = None
        self.app.client.do_process_queue = True

    def call_generate(self, image=None, seed=None):
        if self.generator_section == "txt2img" and self.enable_controlnet and self.controlnet is not None:
            use_pixels = True
        else:
            use_pixels = self.generator_section in (
                "txt2img",
                "pix2pix",
                "depth2img",
                "outpaint",
                "controlnet",
                "superresolution",
                "upscale"
            )

        if use_pixels:
            self.requested_image = image
            self.start_progress_bar()
            image = self.ui.input_image_widget.current_input_image

            if image is None and self.is_txt2img:
                return self.do_generate(seed=seed)
            elif image is None:
                # create a transparent image the size of self.canvas.active_grid_area_rect
                width = self.settings_manager.working_width
                height = self.settings_manager.working_height
                image = Image.new("RGBA", (int(width), int(height)), (0, 0, 0, 0))

            img = image.copy().convert("RGBA")
            new_image = Image.new(
                "RGBA",
                (self.settings_manager.working_width, self.settings_manager.working_height),
                (0, 0, 0))

            cropped_outpaint_box_rect = self.active_rect
            crop_location = (
                cropped_outpaint_box_rect.x() - self.canvas.image_pivot_point.x(),
                cropped_outpaint_box_rect.y() - self.canvas.image_pivot_point.y(),
                cropped_outpaint_box_rect.width() - self.canvas.image_pivot_point.x(),
                cropped_outpaint_box_rect.height() - self.canvas.image_pivot_point.y()
            )
            new_image.paste(img.crop(crop_location), (0, 0))
            # save new_image to disc
            mask = Image.new("RGB", (new_image.width, new_image.height), (255, 255, 255))
            for x in range(new_image.width):
                for y in range(new_image.height):
                    try:
                        if new_image.getpixel((x, y))[3] != 0:
                            mask.putpixel((x, y), (0, 0, 0))
                    except IndexError:
                        pass

            # convert image to rgb
            image = new_image.convert("RGB")
            self.do_generate({
                "mask": mask,
                "image": image,
                "location": self.canvas.active_grid_area_rect
            }, seed=seed)
        elif self.generator_section == "vid2vid":
            images = self.prep_video()
            self.do_generate({
                "images": images
            }, seed=seed)
        else:
            self.do_generate(seed=seed)

    def prep_video(self):
        return []

    def do_generate(self, extra_options=None, seed=None, latents_seed=None):
        if not extra_options:
            extra_options = {}

        if self.enable_controlnet:
            extra_options["input_image"] = self.ui.controlnet_settings.current_controlnet_input_image

        self.set_seed(seed=seed, latents_seed=latents_seed)
        seed = self.seed
        latents_seed = self.latents_seed

        deterministic = self.settings_manager.generator.deterministic
        if self.deterministic_data and deterministic:
            return self.do_deterministic_generation(extra_options)

        action = self.generator_section

        prompt = self.ui.prompt
        negative_prompt = self.ui.negative_prompt

        # set the model data
        model = self.settings_manager.models.filter_by(name=self.ui.model).first()
        model_path = model.path
        model_branch = model.branch
        model_data = {
            "name": model.name,
            "path": model.path,
            "branch": model.branch,
            "version": model.version,
            "category": model.category,
            "pipeline_action": model.pipeline_action,
            "enabled": model.enabled,
            "default": model.default
        }

        # get controlnet_dropdown from active tab
        options = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "steps": self.steps,
            "ddim_eta": self.ddim_eta,  # only applies to ddim scheduler
            "n_iter": 1,
            "n_samples": self.samples,
            "scale": self.scale / 100,
            "seed": seed,
            "latents_seed": latents_seed,
            "model": self.model,
            "model_data": model_data,
            "scheduler": self.scheduler,
            "model_path": model_path,
            "model_branch": model_branch,
            # "lora": self.available_lora(action),
            "controlnet_conditioning_scale": self.settings_manager.generator.controlnet_guidance_scale,
            "generator_section": self.generator_section,
            "width": self.settings_manager.working_width,
            "height": self.settings_manager.working_height,
            "do_nsfw_filter": self.settings_manager.nsfw_filter,
            "pos_x": 0,
            "pos_y": 0,
            "outpaint_box_rect": self.active_rect,
            "hf_token": self.settings_manager.hf_api_key,
            "batch_size": self.ui.deterministic_panel_widget.deterministic_batch_size if self.deterministic else 1,
            "deterministic_generation": self.deterministic,
            "deterministic_style": self.ui.deterministic_panel_widget.deterministic_style,
            "deterministic_seed": None,
            "model_base_path": self.settings_manager.path_settings.model_base_path,
            "outpaint_model_path": self.settings_manager.path_settings.outpaint_model_path,
            "pix2pix_model_path": self.settings_manager.path_settings.pix2pix_model_path,
            "depth2img_model_path": self.settings_manager.path_settings.depth2img_model_path,
            "upscale_model_path": self.settings_manager.path_settings.upscale_model_path,
            "gif_path": self.settings_manager.path_settings.gif_path,
            "image_path": self.settings_manager.path_settings.image_path,
            "lora_path": self.settings_manager.lora_path,
            "embeddings_path": self.settings_manager.path_settings.embeddings_path,
            "video_path": self.settings_manager.path_settings.video_path,
            "clip_skip": self.ui.clip_skip_widget.current_value,
            "variation": self.ui.variation_widget.current_value,
        }

        options["enable_controlnet"] = self.enable_controlnet
        options["controlnet"] = self.controlnet

        if self.controlnet_image:
            options["controlnet_image"] = self.controlnet_image

        if action == "superresolution":
            options["original_image_width"] = self.canvas.current_active_image_data.image.width
            options["original_image_height"] = self.canvas.current_active_image_data.image.height

        if action in ["txt2img", "img2img", "outpaint", "depth2img"]:
            options[f"strength"] = self.strength / 10000.0
        elif action in ["pix2pix"]:
            options[f"image_guidance_scale"] = self.image_scale / 10000.0 * 100.0

        """
        Emitting generate_signal with options allows us to pass more options to the dict from
        modal windows such as the image interpolation window.
        """
        self.app.generate_signal.emit(options)

        memory_options = self.get_memory_options()

        data = {
            "action": action,
            "options": {
                **options,
                **extra_options,
                **memory_options
            }
        }
        self.app.client.message = data

    def do_deterministic_generation(self, extra_options):
        action = self.deterministic_data["action"]
        options = self.deterministic_data["options"]
        options[f"prompt"] = self.deterministic_data[f"prompt"][self.deterministic_index]
        memory_options = self.get_memory_options()
        data = {
            "action": action,
            "options": {
                **options,
                **extra_options,
                **memory_options,
                "batch_size": self.app.deterministic_batch_size,
                "deterministic_generation": True,
                "deterministic_seed": self.app.deterministic_seed,
                "deterministic_style": self.app.deterministic_category
            }
        }
        self.app.client.message = data

    def get_memory_options(self):
        return {
            "use_last_channels": self.settings_manager.memory_settings.use_last_channels,
            "use_enable_sequential_cpu_offload": self.settings_manager.memory_settings.use_enable_sequential_cpu_offload,
            "enable_model_cpu_offload": self.settings_manager.memory_settings.enable_model_cpu_offload,
            "use_attention_slicing": self.settings_manager.memory_settings.use_attention_slicing,
            "use_tf32": self.settings_manager.memory_settings.use_tf32,
            "use_cudnn_benchmark": self.settings_manager.memory_settings.use_cudnn_benchmark,
            "use_enable_vae_slicing": self.settings_manager.memory_settings.use_enable_vae_slicing,
            "use_accelerated_transformers": self.settings_manager.memory_settings.use_accelerated_transformers,
            "use_torch_compile": self.settings_manager.memory_settings.use_torch_compile,
            "use_tiled_vae": self.settings_manager.memory_settings.use_tiled_vae,
        }

    def set_seed(self, seed=None, latents_seed=None):
        """
        Set the seed - either set to random, deterministic or keep current, then display the seed in the UI.
        :return:
        """
        self.set_primary_seed(seed)
        self.set_latents_seed(latents_seed)
        self.update_seed()

    def update_seed(self):
        self.ui.seed_widget.update_seed()
        self.ui.seed_widget_latents.update_seed()

    def set_primary_seed(self, seed=None):
        if self.deterministic_data:
            self.seed = self.deterministic_data["options"][f"seed"]
        elif self.random_seed:
            self.seed = random.randint(0, MAX_SEED)
        elif seed is not None:
            self.seed = seed

    def set_latents_seed(self, latents_seed=None):
        if self.random_latents_seed:
            random.seed()
            latents_seed = random.randint(0, MAX_SEED)
        if latents_seed is not None:
            self.latents_seed = latents_seed

    def start_progress_bar(self):
        self.ui.progress_bar.setRange(0, 0)
        self.app.message_var.emit({
            "message": {
                "step": 0,
                "total": 0,
                "action": self.generator_section,
                "image": None,
                "data": None
            },
            "code": MessageCode.PROGRESS
        })

    def save_db_session(self):
        from airunner.utils import save_session
        save_session()

    def handle_checkbox_change(self, key, widget_name):
        widget = getattr(self.ui, widget_name)
        value = widget.isChecked()
        setattr(self.generator_settings, key, value)
        self.save_db_session()
        self.changed_signal.emit(key, value)

    def initialize(self):
        self.settings_manager.generator_section = self.generator_section
        self.settings_manager.generator_name = self.generator_name
        self.set_form_values()
        self.load_models()
        self.load_schedulers()
        self.set_controlnet_settings_properties()
        self.set_input_image_widget_properties()

        # find all SliderWidget widgets in the template and call initialize
        for widget in self.findChildren(SliderWidget):
            try:
                current_value = getattr(
                    self.generator_settings,
                    widget.property("settings_property").split(".")[1]
                )
            except Exception as e:
                current_value = None
            if current_value is not None:
                widget.setProperty("current_value", current_value)
            widget.initialize()

        self.ui.seed_widget.setProperty("generator_section", self.generator_section)
        self.ui.seed_widget.setProperty("generator_name", self.generator_name)
        self.ui.seed_widget.initialize(
            self.generator_section,
            self.generator_name
        )

        self.ui.seed_widget_latents.setProperty("generator_section", self.generator_section)
        self.ui.seed_widget_latents.setProperty("generator_name", self.generator_name)
        self.ui.seed_widget_latents.initialize(
            self.generator_section,
            self.generator_name
        )
        self.initialized = True

    def set_controlnet_settings_properties(self):
        self.ui.controlnet_settings.initialize(
            self.generator_name,
            self.generator_section
        )

    def set_input_image_widget_properties(self):
        self.ui.input_image_widget.initialize(
            self.generator_name,
            self.generator_section
        )
        self.ui.controlnet_settings.initialize(
            self.generator_name,
            self.generator_section
        )

    def clear_prompts(self):
        self.ui.prompt.setPlainText("")
        self.ui.negative_prompt.setPlainText("")

    def load_models(self):
        self.clear_models()
        requested_section = "txt2img" if self.generator_section == "txt2vid" \
            else self.generator_section
        models = self.settings_manager.available_model_names(
            pipeline_action=requested_section,
            category=self.generator_name)
        self.ui.model.addItems(models)

    def load_schedulers(self):
        session = get_session()
        schedulers = session.query(ActionScheduler).filter(
            ActionScheduler.section == self.generator_section,
            ActionScheduler.generator_name == self.generator_name
        ).all()
        scheduler_names = [s.scheduler.display_name for s in schedulers]
        self.ui.scheduler.addItems(scheduler_names)

    def set_form_values(self):
        self.ui.prompt.setPlainText(self.settings_manager.generator.prompt)
        self.ui.negative_prompt.setPlainText(self.settings_manager.generator.negative_prompt)
        self.ui.use_prompt_builder_checkbox.setChecked(self.settings_manager.generator.use_prompt_builder)

    def clear_models(self):
        self.ui.model.clear()

    def new_batch(self, index, image, data):
        self.new_batch(index, image, data)
        """
        Generate a batch of images using deterministic geneartion based on a previous deterministic generation
        batch. The previous seed that was chosen should be re-used with the index added to it to generate the new
        batch of images.
        :return:
        """
        if not data["options"]["deterministic_seed"]:
            data["options"][f"seed"] = int(data["options"][f"seed"]) + index
            seed = data["options"][f"seed"]
        else:
            seed = data["options"][f"deterministic_seed"]
        self.deterministic_seed = int(seed) + index
        self.deterministic_data = data
        self.deterministic_index = index
        self.deterministic = True
        self.generate(image, seed=self.deterministic_seed)
        self.deterministic = False
        self.deterministic_data = None
        self.deterministic_images = None
