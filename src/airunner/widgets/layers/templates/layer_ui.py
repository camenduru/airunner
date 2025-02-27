# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/layers/templates/layer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LayerWidget(object):
    def setupUi(self, LayerWidget):
        LayerWidget.setObjectName("LayerWidget")
        LayerWidget.resize(669, 54)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayerWidget.sizePolicy().hasHeightForWidth())
        LayerWidget.setSizePolicy(sizePolicy)
        LayerWidget.setMinimumSize(QtCore.QSize(0, 38))
        LayerWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(LayerWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.visible_button = QtWidgets.QPushButton(parent=LayerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visible_button.sizePolicy().hasHeightForWidth())
        self.visible_button.setSizePolicy(sizePolicy)
        self.visible_button.setMinimumSize(QtCore.QSize(38, 38))
        self.visible_button.setMaximumSize(QtCore.QSize(38, 38))
        self.visible_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.visible_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dark/eye-look-icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.visible_button.setIcon(icon)
        self.visible_button.setCheckable(True)
        self.visible_button.setFlat(False)
        self.visible_button.setObjectName("visible_button")
        self.gridLayout.addWidget(self.visible_button, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=LayerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 38))
        self.frame.setStyleSheet("border-color: rgb(51, 209, 122);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.thumbnail = QtWidgets.QLabel(parent=self.frame)
        self.thumbnail.setMinimumSize(QtCore.QSize(38, 38))
        self.thumbnail.setMaximumSize(QtCore.QSize(38, 38))
        self.thumbnail.setText("")
        self.thumbnail.setObjectName("thumbnail")
        self.horizontalLayout_3.addWidget(self.thumbnail)
        self.layer_name = QtWidgets.QLabel(parent=self.frame)
        self.layer_name.setStyleSheet("border-color: rgba(0, 0, 0, 0);")
        self.layer_name.setObjectName("layer_name")
        self.horizontalLayout_3.addWidget(self.layer_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(LayerWidget)
        self.visible_button.clicked.connect(LayerWidget.action_clicked_button_toggle_layer_visibility) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LayerWidget)

    def retranslateUi(self, LayerWidget):
        _translate = QtCore.QCoreApplication.translate
        LayerWidget.setWindowTitle(_translate("LayerWidget", "Form"))
        self.layer_name.setText(_translate("LayerWidget", "Layer 1"))
