# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/breadcrumbs/templates/breadcrumb_container_widget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_breadcrumb_container_widget(object):
    def setupUi(self, breadcrumb_container_widget):
        breadcrumb_container_widget.setObjectName("breadcrumb_container_widget")
        breadcrumb_container_widget.resize(450, 304)
        self.gridLayout = QtWidgets.QGridLayout(breadcrumb_container_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.breadcrumb_container = QtWidgets.QHBoxLayout()
        self.breadcrumb_container.setObjectName("breadcrumb_container")
        self.gridLayout.addLayout(self.breadcrumb_container, 0, 0, 1, 1)

        self.retranslateUi(breadcrumb_container_widget)
        QtCore.QMetaObject.connectSlotsByName(breadcrumb_container_widget)

    def retranslateUi(self, breadcrumb_container_widget):
        _translate = QtCore.QCoreApplication.translate
        breadcrumb_container_widget.setWindowTitle(_translate("breadcrumb_container_widget", "Form"))
