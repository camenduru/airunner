from airunner.widgets.base_widget import BaseWidget
from airunner.widgets.memory_preferences.templates.memory_preferences_ui import Ui_memory_preferences


class MemoryPreferencesWidget(BaseWidget):
    widget_class_ = Ui_memory_preferences

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui.use_accelerated_transformers.blockSignals(True)
        self.ui.use_attention_slicing.blockSignals(True)
        self.ui.use_enable_sequential_cpu_offload.blockSignals(True)
        self.ui.enable_model_cpu_offload.blockSignals(True)
        self.ui.use_lastchannels.blockSignals(True)
        self.ui.use_tf32.blockSignals(True)
        self.ui.use_tiled_vae.blockSignals(True)
        self.ui.use_enable_vae_slicing.blockSignals(True)

        self.ui.use_accelerated_transformers.setChecked(self.settings_manager.memory_settings.use_accelerated_transformers is True)
        self.ui.use_attention_slicing.setChecked(self.settings_manager.memory_settings.use_attention_slicing is True)
        self.ui.use_enable_sequential_cpu_offload.setChecked(
            self.settings_manager.memory_settings.use_enable_sequential_cpu_offload is True)
        self.ui.enable_model_cpu_offload.setChecked(
            self.settings_manager.memory_settings.enable_model_cpu_offload is True
        )
        self.ui.use_lastchannels.setChecked(self.settings_manager.memory_settings.use_last_channels is True)
        self.ui.use_tf32.setChecked(self.settings_manager.memory_settings.use_tf32 is True)
        self.ui.use_tiled_vae.setChecked(self.settings_manager.memory_settings.use_tiled_vae is True)
        self.ui.use_enable_vae_slicing.setChecked(self.settings_manager.memory_settings.use_enable_vae_slicing is True)

        self.ui.use_accelerated_transformers.blockSignals(False)
        self.ui.use_attention_slicing.blockSignals(False)
        self.ui.use_enable_sequential_cpu_offload.blockSignals(False)
        self.ui.enable_model_cpu_offload.blockSignals(False)
        self.ui.use_lastchannels.blockSignals(False)
        self.ui.use_tf32.blockSignals(False)
        self.ui.use_tiled_vae.blockSignals(False)
        self.ui.use_enable_vae_slicing.blockSignals(False)

    def action_toggled_tile_vae(self, val):
        self.settings_manager.set_value("memory_settings.use_tiled_vae", val)

    def action_toggled_tf32(self, val):
        self.settings_manager.set_value("memory_settings.use_tf32", val)

    def action_toggled_last_memory(self, val):
        self.settings_manager.set_value("memory_settings.use_last_channels", val)

    def action_toggled_vae_slicing(self, val):
        self.settings_manager.set_value("memory_settings.use_enable_vae_slicing", val)

    def action_toggled_sequential_cpu_offload(self, val):
        self.settings_manager.set_value("memory_settings.use_enable_sequential_cpu_offload", val)

    def action_toggled_model_cpu_offload(self, val):
        self.settings_manager.set_value("memory_settings.enable_model_cpu_offload", val)

    def action_toggled_attention_slicing(self, val):
        self.settings_manager.set_value("memory_settings.use_attention_slicing", val)

    def action_toggled_accelerated_transformers(self, val):
        self.settings_manager.set_value("memory_settings.use_accelerated_transformers", val)

    def action_button_clicked_optimize_memory_settings(self):
        self.ui.use_accelerated_transformers.setChecked(True)
        self.ui.use_attention_slicing.setChecked(False)
        self.ui.use_lastchannels.setChecked(True)
        self.ui.use_enable_sequential_cpu_offload.setChecked(False)
        self.ui.enable_model_cpu_offload.setChecked(False)
        self.ui.use_tf32.setChecked(False)
        self.ui.use_tiled_vae.setChecked(True)
        self.ui.use_enable_vae_slicing.setChecked(True)
