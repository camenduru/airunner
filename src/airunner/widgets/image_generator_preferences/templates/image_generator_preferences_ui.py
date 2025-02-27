# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/image_generator_preferences/templates/image_generator_preferences.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_image_generator_preferences(object):
    def setupUi(self, image_generator_preferences):
        image_generator_preferences.setObjectName("image_generator_preferences")
        image_generator_preferences.resize(400, 177)
        self.gridLayout = QtWidgets.QGridLayout(image_generator_preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=image_generator_preferences)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stablediffusion = QtWidgets.QRadioButton(parent=self.groupBox)
        self.stablediffusion.setObjectName("stablediffusion")
        self.gridLayout_2.addWidget(self.stablediffusion, 0, 0, 1, 1)
        self.kandinsky = QtWidgets.QRadioButton(parent=self.groupBox)
        self.kandinsky.setObjectName("kandinsky")
        self.gridLayout_2.addWidget(self.kandinsky, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(image_generator_preferences)
        self.stablediffusion.toggled['bool'].connect(image_generator_preferences.stablediffusion_toggled) # type: ignore
        self.kandinsky.toggled['bool'].connect(image_generator_preferences.kandinsky_toggled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(image_generator_preferences)

    def retranslateUi(self, image_generator_preferences):
        _translate = QtCore.QCoreApplication.translate
        image_generator_preferences.setWindowTitle(_translate("image_generator_preferences", "Form"))
        self.groupBox.setTitle(_translate("image_generator_preferences", "Current Image Generator"))
        self.stablediffusion.setText(_translate("image_generator_preferences", "StableDiffusion"))
        self.kandinsky.setText(_translate("image_generator_preferences", "Kandinsky"))
