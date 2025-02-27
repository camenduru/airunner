# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/windows/interpolation/templates/interpolation.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_interpolation_window(object):
    def setupUi(self, interpolation_window):
        interpolation_window.setObjectName("interpolation_window")
        interpolation_window.resize(728, 878)
        self.gridLayout_2 = QtWidgets.QGridLayout(interpolation_window)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.generate_scroll_area = QtWidgets.QScrollArea(parent=interpolation_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_scroll_area.sizePolicy().hasHeightForWidth())
        self.generate_scroll_area.setSizePolicy(sizePolicy)
        self.generate_scroll_area.setMinimumSize(QtCore.QSize(300, 0))
        self.generate_scroll_area.setMaximumSize(QtCore.QSize(300, 16777215))
        self.generate_scroll_area.setWidgetResizable(True)
        self.generate_scroll_area.setObjectName("generate_scroll_area")
        self.generatedScrollArea = QtWidgets.QWidget()
        self.generatedScrollArea.setGeometry(QtCore.QRect(0, 0, 298, 776))
        self.generatedScrollArea.setObjectName("generatedScrollArea")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.generatedScrollArea)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.interpolated_images_label = QtWidgets.QLabel(parent=self.generatedScrollArea)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.interpolated_images_label.setFont(font)
        self.interpolated_images_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.interpolated_images_label.setObjectName("interpolated_images_label")
        self.gridLayout_4.addWidget(self.interpolated_images_label, 0, 0, 1, 1)
        self.generate_scroll_area.setWidget(self.generatedScrollArea)
        self.gridLayout.addWidget(self.generate_scroll_area, 0, 1, 1, 1)
        self.interpolation_scrollarea = QtWidgets.QScrollArea(parent=interpolation_window)
        self.interpolation_scrollarea.setMinimumSize(QtCore.QSize(256, 0))
        self.interpolation_scrollarea.setWidgetResizable(True)
        self.interpolation_scrollarea.setObjectName("interpolation_scrollarea")
        self.interpolation_scrollarea_layout = QtWidgets.QWidget()
        self.interpolation_scrollarea_layout.setGeometry(QtCore.QRect(0, 0, 400, 776))
        self.interpolation_scrollarea_layout.setObjectName("interpolation_scrollarea_layout")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.interpolation_scrollarea_layout)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.interpolation_scrollarea.setWidget(self.interpolation_scrollarea_layout)
        self.gridLayout.addWidget(self.interpolation_scrollarea, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.add_blend_option_button = QtWidgets.QPushButton(parent=interpolation_window)
        self.add_blend_option_button.setObjectName("add_blend_option_button")
        self.gridLayout_2.addWidget(self.add_blend_option_button, 2, 0, 1, 1)
        self.generate_frame = QtWidgets.QFrame(parent=interpolation_window)
        self.generate_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.generate_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.generate_frame.setObjectName("generate_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.generate_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.generate_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.kandinsky_button = QtWidgets.QPushButton(parent=self.generate_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kandinsky_button.setFont(font)
        self.kandinsky_button.setObjectName("kandinsky_button")
        self.gridLayout_5.addWidget(self.kandinsky_button, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.generate_frame, 0, 0, 1, 1)

        self.retranslateUi(interpolation_window)
        QtCore.QMetaObject.connectSlotsByName(interpolation_window)

    def retranslateUi(self, interpolation_window):
        _translate = QtCore.QCoreApplication.translate
        interpolation_window.setWindowTitle(_translate("interpolation_window", "Image Interpolation"))
        self.interpolated_images_label.setText(_translate("interpolation_window", "Interpolated images will appear here"))
        self.add_blend_option_button.setText(_translate("interpolation_window", "Add blend option"))
        self.label_2.setText(_translate("interpolation_window", "Interpolation is currently only compatible with the Kandinsky txt2img generator."))
        self.kandinsky_button.setText(_translate("interpolation_window", "Activate Kandinsky tab"))
