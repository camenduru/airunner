# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/windows/about/templates/about.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(270, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(about_window.sizePolicy().hasHeightForWidth())
        about_window.setSizePolicy(sizePolicy)
        about_window.setMinimumSize(QtCore.QSize(270, 150))
        about_window.setMaximumSize(QtCore.QSize(270, 150))
        self.layoutWidget = QtWidgets.QWidget(parent=about_window)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 249, 134))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.title = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.title)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.buttonBox)

        self.retranslateUi(about_window)
        self.buttonBox.accepted.connect(about_window.accept) # type: ignore
        self.buttonBox.rejected.connect(about_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "About"))
        self.title.setText(_translate("about_window", "AI Runner v"))
        self.label_3.setText(_translate("about_window", "Powered by open source software"))
        self.label_2.setText(_translate("about_window", "Copyright © 2022-2023 Capsize LLC"))
