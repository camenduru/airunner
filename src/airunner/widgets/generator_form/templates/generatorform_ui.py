# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/generator_form/templates/generatorform.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_generator_form(object):
    def setupUi(self, generator_form):
        generator_form.setObjectName("generator_form")
        generator_form.resize(495, 926)
        font = QtGui.QFont()
        font.setPointSize(8)
        generator_form.setFont(font)
        generator_form.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.gridLayout_4 = QtWidgets.QGridLayout(generator_form)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.generator_form_tab_widget = QtWidgets.QTabWidget(parent=generator_form)
        self.generator_form_tab_widget.setObjectName("generator_form_tab_widget")
        self.basic_tab = QtWidgets.QWidget()
        self.basic_tab.setObjectName("basic_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.basic_tab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.basic_widget_contents = QtWidgets.QWidget(parent=self.basic_tab)
        self.basic_widget_contents.setObjectName("basic_widget_contents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.basic_widget_contents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.basic_widget_contents)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.model_2 = QtWidgets.QComboBox(parent=self.basic_widget_contents)
        self.model_2.setObjectName("model_2")
        self.verticalLayout_7.addWidget(self.model_2)
        self.gridLayout_7.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(parent=self.basic_widget_contents)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.use_prompt_builder_checkbox_2 = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.use_prompt_builder_checkbox_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.use_prompt_builder_checkbox_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.use_prompt_builder_checkbox_2.setObjectName("use_prompt_builder_checkbox_2")
        self.horizontalLayout_8.addWidget(self.use_prompt_builder_checkbox_2)
        self.prompt_builder_settings_button_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.prompt_builder_settings_button_2.setMinimumSize(QtCore.QSize(24, 24))
        self.prompt_builder_settings_button_2.setMaximumSize(QtCore.QSize(24, 24))
        self.prompt_builder_settings_button_2.setBaseSize(QtCore.QSize(0, 0))
        self.prompt_builder_settings_button_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.prompt_builder_settings_button_2.setText("")
        icon = QtGui.QIcon.fromTheme("preferences-desktop")
        self.prompt_builder_settings_button_2.setIcon(icon)
        self.prompt_builder_settings_button_2.setFlat(True)
        self.prompt_builder_settings_button_2.setObjectName("prompt_builder_settings_button_2")
        self.horizontalLayout_8.addWidget(self.prompt_builder_settings_button_2)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.basic_prompt = QtWidgets.QPlainTextEdit(parent=self.layoutWidget)
        self.basic_prompt.setObjectName("basic_prompt")
        self.gridLayout_5.addWidget(self.basic_prompt, 1, 0, 1, 2)
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.negative_prompt_2 = QtWidgets.QPlainTextEdit(parent=self.layoutWidget_3)
        self.negative_prompt_2.setObjectName("negative_prompt_2")
        self.verticalLayout_8.addWidget(self.negative_prompt_2)
        self.gridLayout_7.addWidget(self.splitter, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.basic_widget_contents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.basic_widget_contents, 0, 0, 1, 1)
        self.generator_form_tab_widget.addTab(self.basic_tab, "")
        self.advanced_tab = QtWidgets.QWidget()
        self.advanced_tab.setObjectName("advanced_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.advanced_tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.advanced_tab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 491, 861))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.scrollAreaWidgetContents)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.use_prompt_builder_checkbox = QtWidgets.QCheckBox(parent=self.layoutWidget1)
        self.use_prompt_builder_checkbox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.use_prompt_builder_checkbox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.use_prompt_builder_checkbox.setObjectName("use_prompt_builder_checkbox")
        self.horizontalLayout_6.addWidget(self.use_prompt_builder_checkbox)
        self.prompt_builder_settings_button = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.prompt_builder_settings_button.setMinimumSize(QtCore.QSize(24, 24))
        self.prompt_builder_settings_button.setMaximumSize(QtCore.QSize(24, 24))
        self.prompt_builder_settings_button.setBaseSize(QtCore.QSize(0, 0))
        self.prompt_builder_settings_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.prompt_builder_settings_button.setText("")
        icon = QtGui.QIcon.fromTheme("preferences-desktop")
        self.prompt_builder_settings_button.setIcon(icon)
        self.prompt_builder_settings_button.setFlat(True)
        self.prompt_builder_settings_button.setObjectName("prompt_builder_settings_button")
        self.horizontalLayout_6.addWidget(self.prompt_builder_settings_button)
        self.pushButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.prompt = QtWidgets.QPlainTextEdit(parent=self.layoutWidget1)
        self.prompt.setObjectName("prompt")
        self.gridLayout_2.addWidget(self.prompt, 1, 0, 1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.negative_prompt = QtWidgets.QPlainTextEdit(parent=self.layoutWidget2)
        self.negative_prompt.setObjectName("negative_prompt")
        self.verticalLayout_6.addWidget(self.negative_prompt)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.splitter_2)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 473, 172))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.model = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents_5)
        self.model.setObjectName("model")
        self.verticalLayout.addWidget(self.model)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.scheduler = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents_5)
        self.scheduler.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.scheduler.setObjectName("scheduler")
        self.verticalLayout_2.addWidget(self.scheduler)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.variation_checkbox = QtWidgets.QCheckBox(parent=self.scrollAreaWidgetContents_5)
        self.variation_checkbox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.variation_checkbox.setObjectName("variation_checkbox")
        self.verticalLayout_5.addWidget(self.variation_checkbox)
        self.gridLayout.addLayout(self.verticalLayout_5, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.steps_widget = SliderWidget(parent=self.scrollAreaWidgetContents_5)
        self.steps_widget.setProperty("slider_callback", "handle_value_change")
        self.steps_widget.setProperty("current_value", 0)
        self.steps_widget.setProperty("slider_maximum", 200)
        self.steps_widget.setProperty("spinbox_maximum", 200.0)
        self.steps_widget.setProperty("display_as_float", False)
        self.steps_widget.setProperty("spinbox_single_step", 1)
        self.steps_widget.setProperty("spinbox_page_step", 1)
        self.steps_widget.setProperty("spinbox_minimum", 1)
        self.steps_widget.setProperty("slider_minimum", 1)
        self.steps_widget.setProperty("settings_property", "generator.steps")
        self.steps_widget.setObjectName("steps_widget")
        self.horizontalLayout_2.addWidget(self.steps_widget)
        self.scale_widget = SliderWidget(parent=self.scrollAreaWidgetContents_5)
        self.scale_widget.setProperty("current_value", 0)
        self.scale_widget.setProperty("slider_maximum", 10000)
        self.scale_widget.setProperty("spinbox_maximum", 100.0)
        self.scale_widget.setProperty("display_as_float", True)
        self.scale_widget.setProperty("spinbox_single_step", 0.01)
        self.scale_widget.setProperty("spinbox_page_step", 0.01)
        self.scale_widget.setProperty("slider_callback", "handle_value_change")
        self.scale_widget.setProperty("settings_property", "generator.scale")
        self.scale_widget.setObjectName("scale_widget")
        self.horizontalLayout_2.addWidget(self.scale_widget)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.samples_widget = SliderWidget(parent=self.scrollAreaWidgetContents_5)
        self.samples_widget.setProperty("slider_callback", "handle_value_change")
        self.samples_widget.setProperty("current_value", 0)
        self.samples_widget.setProperty("slider_maximum", 500)
        self.samples_widget.setProperty("spinbox_maximum", 500.0)
        self.samples_widget.setProperty("display_as_float", False)
        self.samples_widget.setProperty("spinbox_single_step", 1)
        self.samples_widget.setProperty("spinbox_page_step", 1)
        self.samples_widget.setProperty("spinbox_minimum", 1)
        self.samples_widget.setProperty("slider_minimum", 1)
        self.samples_widget.setObjectName("samples_widget")
        self.horizontalLayout_4.addWidget(self.samples_widget)
        self.clip_skip_slider_widget = SliderWidget(parent=self.scrollAreaWidgetContents_5)
        self.clip_skip_slider_widget.setProperty("current_value", 0)
        self.clip_skip_slider_widget.setProperty("slider_maximum", 11)
        self.clip_skip_slider_widget.setProperty("spinbox_maximum", 12.0)
        self.clip_skip_slider_widget.setProperty("display_as_float", False)
        self.clip_skip_slider_widget.setProperty("spinbox_single_step", 1)
        self.clip_skip_slider_widget.setProperty("spinbox_page_step", 1)
        self.clip_skip_slider_widget.setProperty("spinbox_minimum", 0)
        self.clip_skip_slider_widget.setProperty("slider_minimum", 0)
        self.clip_skip_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.clip_skip_slider_widget.setProperty("settings_property", "generator.clip_skip")
        self.clip_skip_slider_widget.setObjectName("clip_skip_slider_widget")
        self.horizontalLayout_4.addWidget(self.clip_skip_slider_widget)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ddim_eta_slider_widget = SliderWidget(parent=self.scrollAreaWidgetContents_5)
        self.ddim_eta_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.ddim_eta_slider_widget.setProperty("current_value", 1)
        self.ddim_eta_slider_widget.setProperty("slider_maximum", 10)
        self.ddim_eta_slider_widget.setProperty("spinbox_maximum", 10)
        self.ddim_eta_slider_widget.setProperty("display_as_float", False)
        self.ddim_eta_slider_widget.setProperty("spinbox_single_step", 1)
        self.ddim_eta_slider_widget.setProperty("spinbox_page_step", 1)
        self.ddim_eta_slider_widget.setProperty("spinbox_minimum", 1)
        self.ddim_eta_slider_widget.setProperty("slider_minimum", 1)
        self.ddim_eta_slider_widget.setProperty("settings_property", "generator.ddim_eta")
        self.ddim_eta_slider_widget.setObjectName("ddim_eta_slider_widget")
        self.horizontalLayout_7.addWidget(self.ddim_eta_slider_widget)
        self.frames_slider_widget = SliderWidget(parent=self.scrollAreaWidgetContents_5)
        self.frames_slider_widget.setProperty("slider_callback", "handle_value_change")
        self.frames_slider_widget.setProperty("current_value", 0)
        self.frames_slider_widget.setProperty("slider_maximum", 200)
        self.frames_slider_widget.setProperty("spinbox_maximum", 200.0)
        self.frames_slider_widget.setProperty("display_as_float", False)
        self.frames_slider_widget.setProperty("spinbox_single_step", 1)
        self.frames_slider_widget.setProperty("spinbox_page_step", 1)
        self.frames_slider_widget.setProperty("spinbox_minimum", 1)
        self.frames_slider_widget.setProperty("slider_minimum", 1)
        self.frames_slider_widget.setProperty("settings_property", "generator.n_samples")
        self.frames_slider_widget.setObjectName("frames_slider_widget")
        self.horizontalLayout_7.addWidget(self.frames_slider_widget)
        self.gridLayout.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.seed_widget = SeedWidget(parent=self.scrollAreaWidgetContents_5)
        self.seed_widget.setProperty("generator_section", "")
        self.seed_widget.setProperty("generator_name", "")
        self.seed_widget.setObjectName("seed_widget")
        self.horizontalLayout.addWidget(self.seed_widget)
        self.seed_widget_latents = LatentsSeedWidget(parent=self.scrollAreaWidgetContents_5)
        self.seed_widget_latents.setProperty("generator_section", "")
        self.seed_widget_latents.setProperty("generator_name", "")
        self.seed_widget_latents.setObjectName("seed_widget_latents")
        self.horizontalLayout.addWidget(self.seed_widget_latents)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.input_image_widget = InputImageSettingsWidget(parent=self.scrollAreaWidgetContents_5)
        self.input_image_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.input_image_widget.setAcceptDrops(False)
        self.input_image_widget.setProperty("generator_section", "")
        self.input_image_widget.setProperty("generator_name", "")
        self.input_image_widget.setObjectName("input_image_widget")
        self.verticalLayout_3.addWidget(self.input_image_widget)
        self.controlnet_settings = ControlNetSettingsWidget(parent=self.scrollAreaWidgetContents_5)
        self.controlnet_settings.setMinimumSize(QtCore.QSize(0, 0))
        self.controlnet_settings.setAcceptDrops(False)
        self.controlnet_settings.setProperty("generator_section", "")
        self.controlnet_settings.setProperty("generator_name", "")
        self.controlnet_settings.setObjectName("controlnet_settings")
        self.verticalLayout_3.addWidget(self.controlnet_settings)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_8.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.generator_form_tab_widget.addTab(self.advanced_tab, "")
        self.gridLayout_4.addWidget(self.generator_form_tab_widget, 0, 0, 1, 1)
        self.generator_container = QtWidgets.QWidget(parent=generator_form)
        self.generator_container.setObjectName("generator_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.generator_container)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.generate_button = QtWidgets.QPushButton(parent=self.generator_container)
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout_3.addWidget(self.generate_button)
        self.progress_bar = QtWidgets.QProgressBar(parent=self.generator_container)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout_3.addWidget(self.progress_bar)
        self.interrupt_button = QtWidgets.QPushButton(parent=self.generator_container)
        self.interrupt_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.interrupt_button.setObjectName("interrupt_button")
        self.horizontalLayout_3.addWidget(self.interrupt_button)
        self.gridLayout_4.addWidget(self.generator_container, 1, 0, 1, 1)

        self.retranslateUi(generator_form)
        self.generator_form_tab_widget.setCurrentIndex(1)
        self.prompt.textChanged.connect(generator_form.handle_prompt_changed) # type: ignore
        self.negative_prompt.textChanged.connect(generator_form.handle_negative_prompt_changed) # type: ignore
        self.use_prompt_builder_checkbox.toggled['bool'].connect(generator_form.toggle_prompt_builder_checkbox) # type: ignore
        self.model.currentTextChanged['QString'].connect(generator_form.handle_model_changed) # type: ignore
        self.scheduler.currentTextChanged['QString'].connect(generator_form.handle_scheduler_changed) # type: ignore
        self.variation_checkbox.toggled['bool'].connect(generator_form.toggle_variation) # type: ignore
        self.pushButton.clicked.connect(generator_form.action_clicked_button_save_prompts) # type: ignore
        self.basic_prompt.textChanged.connect(generator_form.handle_prompt_changed) # type: ignore
        self.negative_prompt_2.textChanged.connect(generator_form.handle_negative_prompt_changed) # type: ignore
        self.pushButton_2.clicked.connect(generator_form.action_clicked_button_save_prompts) # type: ignore
        self.model_2.currentTextChanged['QString'].connect(generator_form.handle_model_changed) # type: ignore
        self.use_prompt_builder_checkbox_2.toggled['bool'].connect(generator_form.toggle_prompt_builder_checkbox) # type: ignore
        self.generate_button.clicked.connect(generator_form.handle_generate_button_clicked) # type: ignore
        self.interrupt_button.clicked.connect(generator_form.handle_interrupt_button_clicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(generator_form)

    def retranslateUi(self, generator_form):
        _translate = QtCore.QCoreApplication.translate
        generator_form.setWindowTitle(_translate("generator_form", "Form"))
        self.label_5.setText(_translate("generator_form", "Model"))
        self.label_7.setText(_translate("generator_form", "Prompt"))
        self.use_prompt_builder_checkbox_2.setText(_translate("generator_form", "Use Prompt Builder"))
        self.basic_prompt.setPlaceholderText(_translate("generator_form", "Enter a prompt..."))
        self.label_6.setText(_translate("generator_form", "Negative Prompt"))
        self.negative_prompt_2.setPlaceholderText(_translate("generator_form", "Enter a negative prompt..."))
        self.pushButton_2.setText(_translate("generator_form", "Save Prompts"))
        self.generator_form_tab_widget.setTabText(self.generator_form_tab_widget.indexOf(self.basic_tab), _translate("generator_form", "Basic"))
        self.label.setText(_translate("generator_form", "Prompt"))
        self.use_prompt_builder_checkbox.setText(_translate("generator_form", "Use Prompt Builder"))
        self.pushButton.setText(_translate("generator_form", "Save Prompts"))
        self.prompt.setPlaceholderText(_translate("generator_form", "Enter a prompt..."))
        self.label_2.setText(_translate("generator_form", "Negative Prompt"))
        self.negative_prompt.setPlaceholderText(_translate("generator_form", "Enter a negative prompt..."))
        self.label_3.setText(_translate("generator_form", "Model"))
        self.label_4.setText(_translate("generator_form", "Scheduler"))
        self.variation_checkbox.setText(_translate("generator_form", "Variation"))
        self.steps_widget.setProperty("label_text", _translate("generator_form", "Steps"))
        self.scale_widget.setProperty("label_text", _translate("generator_form", "Scale"))
        self.samples_widget.setProperty("label_text", _translate("generator_form", "Samples"))
        self.samples_widget.setProperty("settings_property", _translate("generator_form", "generator.n_samples"))
        self.clip_skip_slider_widget.setProperty("label_text", _translate("generator_form", "Clip Skip"))
        self.ddim_eta_slider_widget.setProperty("label_text", _translate("generator_form", "DDIM ETA"))
        self.frames_slider_widget.setProperty("label_text", _translate("generator_form", "Frames"))
        self.input_image_widget.setProperty("checkbox_label", _translate("generator_form", "Use Input Image"))
        self.controlnet_settings.setProperty("checkbox_label", _translate("generator_form", "Controlnet"))
        self.generator_form_tab_widget.setTabText(self.generator_form_tab_widget.indexOf(self.advanced_tab), _translate("generator_form", "Advanced"))
        self.generate_button.setText(_translate("generator_form", "Generate"))
        self.interrupt_button.setText(_translate("generator_form", "Interrupt"))
from airunner.widgets.controlnet_settings.controlnet_settings_widget import ControlNetSettingsWidget
from airunner.widgets.input_image.input_image_settings_widget import InputImageSettingsWidget
from airunner.widgets.seed.seed_widget import LatentsSeedWidget, SeedWidget
from airunner.widgets.slider.slider_widget import SliderWidget
