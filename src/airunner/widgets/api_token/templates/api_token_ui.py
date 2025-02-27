# Form implementation generated from reading ui file '/home/joe/Projects/imagetopixel/airunner/src/airunner/../../src/airunner/widgets/api_token/templates/api_token.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_api_token(object):
    def setupUi(self, api_token):
        api_token.setObjectName("api_token")
        api_token.resize(400, 409)
        self.gridLayout = QtWidgets.QGridLayout(api_token)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=api_token)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hf_api_key_writetoken = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.hf_api_key_writetoken.setObjectName("hf_api_key_writetoken")
        self.gridLayout_3.addWidget(self.hf_api_key_writetoken, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=api_token)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=api_token)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=api_token)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=api_token)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hf_api_key_text_generation = QtWidgets.QLineEdit(parent=self.groupBox)
        self.hf_api_key_text_generation.setObjectName("hf_api_key_text_generation")
        self.gridLayout_2.addWidget(self.hf_api_key_text_generation, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=api_token)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=api_token)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.retranslateUi(api_token)
        self.hf_api_key_text_generation.textEdited['QString'].connect(api_token.action_text_edited_api_key) # type: ignore
        self.hf_api_key_writetoken.textEdited['QString'].connect(api_token.action_text_edited_writekey) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(api_token)

    def retranslateUi(self, api_token):
        _translate = QtCore.QCoreApplication.translate
        api_token.setWindowTitle(_translate("api_token", "Form"))
        self.groupBox_2.setTitle(_translate("api_token", "Write token"))
        self.label_3.setText(_translate("api_token", "Huggingface Access Tokens"))
        self.label_2.setText(_translate("api_token", "https://huggingface.co/settings/tokens"))
        self.groupBox.setTitle(_translate("api_token", "Read token"))
        self.label.setText(_translate("api_token", "Get your Huggingface read API token by creating an account on huggingface.co then navigating to"))
