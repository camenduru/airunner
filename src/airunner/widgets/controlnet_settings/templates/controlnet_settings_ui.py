# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/controlnet_settings/templates/controlnet_settings.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_controlnet_settings(object):
    def setupUi(self, controlnet_settings):
        controlnet_settings.setObjectName("controlnet_settings")
        controlnet_settings.resize(294, 181)
        controlnet_settings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        controlnet_settings.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(controlnet_settings)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=controlnet_settings)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.groupBox.setStyleSheet("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(9, -1, 9, 9)
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget = QtWidgets.QWidget(parent=self.groupBox)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.widget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 124))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image_thumbnail = QtWidgets.QPushButton(parent=self.tab_7)
        self.image_thumbnail.setMinimumSize(QtCore.QSize(72, 72))
        self.image_thumbnail.setMaximumSize(QtCore.QSize(72, 72))
        self.image_thumbnail.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.image_thumbnail.setStyleSheet("")
        self.image_thumbnail.setText("")
        self.image_thumbnail.setIconSize(QtCore.QSize(92, 92))
        self.image_thumbnail.setObjectName("image_thumbnail")
        self.gridLayout_2.addWidget(self.image_thumbnail, 0, 0, 2, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.link_settings_button = QtWidgets.QPushButton(parent=self.tab_7)
        self.link_settings_button.setMinimumSize(QtCore.QSize(26, 26))
        self.link_settings_button.setMaximumSize(QtCore.QSize(26, 26))
        self.link_settings_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.link_settings_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/048-chain-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.link_settings_button.setIcon(icon)
        self.link_settings_button.setCheckable(True)
        self.link_settings_button.setChecked(True)
        self.link_settings_button.setFlat(True)
        self.link_settings_button.setObjectName("link_settings_button")
        self.horizontalLayout_2.addWidget(self.link_settings_button)
        self.use_imported_image_button = QtWidgets.QPushButton(parent=self.tab_7)
        self.use_imported_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.use_imported_image_button.setMaximumSize(QtCore.QSize(26, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.use_imported_image_button.setFont(font)
        self.use_imported_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.use_imported_image_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/046-import-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.use_imported_image_button.setIcon(icon1)
        self.use_imported_image_button.setCheckable(True)
        self.use_imported_image_button.setFlat(True)
        self.use_imported_image_button.setObjectName("use_imported_image_button")
        self.horizontalLayout_2.addWidget(self.use_imported_image_button)
        self.use_grid_image_button = QtWidgets.QPushButton(parent=self.tab_7)
        self.use_grid_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.use_grid_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.use_grid_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.use_grid_image_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/025-gallery-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.use_grid_image_button.setIcon(icon2)
        self.use_grid_image_button.setCheckable(True)
        self.use_grid_image_button.setChecked(True)
        self.use_grid_image_button.setFlat(True)
        self.use_grid_image_button.setObjectName("use_grid_image_button")
        self.horizontalLayout_2.addWidget(self.use_grid_image_button)
        self.recycle_grid_image_button = QtWidgets.QPushButton(parent=self.tab_7)
        self.recycle_grid_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.recycle_grid_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.recycle_grid_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.recycle_grid_image_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/047-recycle-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.recycle_grid_image_button.setIcon(icon3)
        self.recycle_grid_image_button.setCheckable(True)
        self.recycle_grid_image_button.setFlat(True)
        self.recycle_grid_image_button.setObjectName("recycle_grid_image_button")
        self.horizontalLayout_2.addWidget(self.recycle_grid_image_button)
        self.refresh_input_image_button = QtWidgets.QPushButton(parent=self.tab_7)
        self.refresh_input_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.refresh_input_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.refresh_input_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.refresh_input_image_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/050-refresh-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.refresh_input_image_button.setIcon(icon4)
        self.refresh_input_image_button.setFlat(True)
        self.refresh_input_image_button.setObjectName("refresh_input_image_button")
        self.horizontalLayout_2.addWidget(self.refresh_input_image_button)
        self.clear_image_button = QtWidgets.QPushButton(parent=self.tab_7)
        self.clear_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.clear_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.clear_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_image_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/006-trash-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.clear_image_button.setIcon(icon5)
        self.clear_image_button.setFlat(True)
        self.clear_image_button.setObjectName("clear_image_button")
        self.horizontalLayout_2.addWidget(self.clear_image_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.import_image_button = QtWidgets.QCommandLinkButton(parent=self.tab_7)
        self.import_image_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_image_button.sizePolicy().hasHeightForWidth())
        self.import_image_button.setSizePolicy(sizePolicy)
        self.import_image_button.setMinimumSize(QtCore.QSize(10, 35))
        self.import_image_button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.import_image_button.setFont(font)
        self.import_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.import_image_button.setObjectName("import_image_button")
        self.gridLayout_2.addWidget(self.import_image_button, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mask_thumbnail = QtWidgets.QPushButton(parent=self.tab_8)
        self.mask_thumbnail.setMinimumSize(QtCore.QSize(72, 72))
        self.mask_thumbnail.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mask_thumbnail.setStyleSheet("")
        self.mask_thumbnail.setText("")
        self.mask_thumbnail.setIconSize(QtCore.QSize(72, 72))
        self.mask_thumbnail.setObjectName("mask_thumbnail")
        self.gridLayout_4.addWidget(self.mask_thumbnail, 0, 0, 2, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mask_link_to_input_image_button = QtWidgets.QPushButton(parent=self.tab_8)
        self.mask_link_to_input_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.mask_link_to_input_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.mask_link_to_input_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mask_link_to_input_image_button.setText("")
        self.mask_link_to_input_image_button.setIcon(icon)
        self.mask_link_to_input_image_button.setCheckable(True)
        self.mask_link_to_input_image_button.setFlat(True)
        self.mask_link_to_input_image_button.setObjectName("mask_link_to_input_image_button")
        self.horizontalLayout_3.addWidget(self.mask_link_to_input_image_button)
        self.mask_use_imported_image_button = QtWidgets.QPushButton(parent=self.tab_8)
        self.mask_use_imported_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.mask_use_imported_image_button.setMaximumSize(QtCore.QSize(26, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.mask_use_imported_image_button.setFont(font)
        self.mask_use_imported_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mask_use_imported_image_button.setText("")
        self.mask_use_imported_image_button.setIcon(icon1)
        self.mask_use_imported_image_button.setCheckable(True)
        self.mask_use_imported_image_button.setFlat(True)
        self.mask_use_imported_image_button.setObjectName("mask_use_imported_image_button")
        self.horizontalLayout_3.addWidget(self.mask_use_imported_image_button)
        self.mask_export_image_button = QtWidgets.QPushButton(parent=self.tab_8)
        self.mask_export_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.mask_export_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.mask_export_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mask_export_image_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/export-light.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.mask_export_image_button.setIcon(icon6)
        self.mask_export_image_button.setCheckable(False)
        self.mask_export_image_button.setFlat(True)
        self.mask_export_image_button.setObjectName("mask_export_image_button")
        self.horizontalLayout_3.addWidget(self.mask_export_image_button)
        self.mask_clear_image_button = QtWidgets.QPushButton(parent=self.tab_8)
        self.mask_clear_image_button.setMinimumSize(QtCore.QSize(26, 26))
        self.mask_clear_image_button.setMaximumSize(QtCore.QSize(26, 26))
        self.mask_clear_image_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mask_clear_image_button.setText("")
        self.mask_clear_image_button.setIcon(icon5)
        self.mask_clear_image_button.setFlat(True)
        self.mask_clear_image_button.setObjectName("mask_clear_image_button")
        self.horizontalLayout_3.addWidget(self.mask_clear_image_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.mask_import_button = QtWidgets.QCommandLinkButton(parent=self.tab_8)
        self.mask_import_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mask_import_button.sizePolicy().hasHeightForWidth())
        self.mask_import_button.setSizePolicy(sizePolicy)
        self.mask_import_button.setMinimumSize(QtCore.QSize(10, 0))
        self.mask_import_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.mask_import_button.setFont(font)
        self.mask_import_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mask_import_button.setObjectName("mask_import_button")
        self.gridLayout_4.addWidget(self.mask_import_button, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 2, 0, 1, 1)
        self.scale_slider_widget = SliderWidget(parent=self.groupBox)
        self.scale_slider_widget.setProperty("current_value", 0)
        self.scale_slider_widget.setProperty("slider_maximum", 100)
        self.scale_slider_widget.setProperty("spinbox_maximum", 1.0)
        self.scale_slider_widget.setProperty("display_as_float", True)
        self.scale_slider_widget.setProperty("spinbox_single_step", 0.01)
        self.scale_slider_widget.setProperty("spinbox_page_step", 0.1)
        self.scale_slider_widget.setProperty("spinbox_minimum", 0.0)
        self.scale_slider_widget.setProperty("slider_minimum", 0)
        self.scale_slider_widget.setObjectName("scale_slider_widget")
        self.gridLayout_5.addWidget(self.scale_slider_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(controlnet_settings)
        self.tabWidget.setCurrentIndex(0)
        self.groupBox.toggled['bool'].connect(controlnet_settings.action_toggled_use_controlnet) # type: ignore
        self.import_image_button.clicked.connect(controlnet_settings.action_clicked_button_import_image) # type: ignore
        self.link_settings_button.toggled['bool'].connect(controlnet_settings.action_toggled_button_link_input_image) # type: ignore
        self.use_imported_image_button.toggled['bool'].connect(controlnet_settings.action_toggled_use_input_image) # type: ignore
        self.use_grid_image_button.toggled['bool'].connect(controlnet_settings.action_toggled_button_use_grid_image) # type: ignore
        self.recycle_grid_image_button.toggled['bool'].connect(controlnet_settings.action_toggled_button_lock_grid_image) # type: ignore
        self.refresh_input_image_button.clicked.connect(controlnet_settings.action_clicked_button_refresh_grid_image) # type: ignore
        self.clear_image_button.clicked.connect(controlnet_settings.action_clicked_button_clear_input_image) # type: ignore
        self.mask_import_button.clicked.connect(controlnet_settings.action_clicked_button_import_image_mask) # type: ignore
        self.mask_link_to_input_image_button.toggled['bool'].connect(controlnet_settings.action_toggled_button_link_input_image_mask) # type: ignore
        self.mask_use_imported_image_button.toggled['bool'].connect(controlnet_settings.action_toggled_use_input_image) # type: ignore
        self.mask_export_image_button.clicked.connect(controlnet_settings.action_clicked_button_export_mask) # type: ignore
        self.mask_clear_image_button.clicked.connect(controlnet_settings.action_clicked_button_clear_input_image_mask) # type: ignore
        self.mask_thumbnail.clicked.connect(controlnet_settings.action_clicked_button_thumbnail_mask) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(controlnet_settings)

    def retranslateUi(self, controlnet_settings):
        _translate = QtCore.QCoreApplication.translate
        controlnet_settings.setWindowTitle(_translate("controlnet_settings", "Form"))
        self.groupBox.setTitle(_translate("controlnet_settings", "Use ControlNet"))
        self.link_settings_button.setToolTip(_translate("controlnet_settings", "Use the main Input Image for the ControlNet input image"))
        self.use_imported_image_button.setToolTip(_translate("controlnet_settings", "Toggle imported input image"))
        self.use_grid_image_button.setToolTip(_translate("controlnet_settings", "Toggle active grid input image"))
        self.recycle_grid_image_button.setToolTip(_translate("controlnet_settings", "Toggle reuse current input image"))
        self.refresh_input_image_button.setToolTip(_translate("controlnet_settings", "Refresh current input image"))
        self.clear_image_button.setToolTip(_translate("controlnet_settings", "Clear imported input imagea"))
        self.import_image_button.setText(_translate("controlnet_settings", "Import image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("controlnet_settings", "Input Image"))
        self.mask_link_to_input_image_button.setToolTip(_translate("controlnet_settings", "Create a mask image based on the ControlNet Input Image"))
        self.mask_use_imported_image_button.setToolTip(_translate("controlnet_settings", "Import a mask image from disk"))
        self.mask_export_image_button.setToolTip(_translate("controlnet_settings", "Export a generated mask image to disk"))
        self.mask_clear_image_button.setToolTip(_translate("controlnet_settings", "Clear the mask image"))
        self.mask_import_button.setText(_translate("controlnet_settings", "Import image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("controlnet_settings", "Mask"))
        self.scale_slider_widget.setProperty("label_text", _translate("controlnet_settings", "Scale"))
        self.scale_slider_widget.setProperty("slider_callback", _translate("controlnet_settings", "handle_value_change"))
        self.scale_slider_widget.setProperty("settings_property", _translate("controlnet_settings", "generator.controlnet_guidance_scale"))
from airunner.widgets.slider.slider_widget import SliderWidget
