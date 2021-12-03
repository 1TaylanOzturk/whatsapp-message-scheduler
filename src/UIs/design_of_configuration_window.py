from PyQt5 import QtCore, QtWidgets


class UI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.setEnabled(True)
        GUI.resize(497, 447)
        GUI.setAutoFillBackground(False)
        self.phoneNumber = QtWidgets.QLineEdit(GUI)
        self.phoneNumber.setGeometry(QtCore.QRect(90, 60, 341, 28))
        self.phoneNumber.setObjectName("phoneNumber")
        self.message = QtWidgets.QPlainTextEdit(GUI)
        self.message.setGeometry(QtCore.QRect(90, 100, 341, 60))
        self.message.setObjectName("message")
        self.label = QtWidgets.QLabel(GUI)
        self.label.setGeometry(QtCore.QRect(210, 30, 100, 16))
        self.label.setStyleSheet("QLabel {\n"
"  font-size: 20px;\n"
"}")
        self.label.setObjectName("label")
        self.hour = QtWidgets.QLineEdit(GUI)
        self.hour.setGeometry(QtCore.QRect(90, 240, 341, 28))
        self.hour.setObjectName("hour")
        self.label_2 = QtWidgets.QLabel(GUI)
        self.label_2.setGeometry(QtCore.QRect(180, 210, 200, 25))
        self.label_2.setStyleSheet("QLabel {\n"
"  font-size: 20px;\n"
"}")
        self.label_2.setObjectName("label_2")
        
        self.minute = QtWidgets.QLineEdit(GUI)
        self.minute.setGeometry(QtCore.QRect(90, 280, 341, 28))
        self.minute.setObjectName("minute")
        self.btn_save = QtWidgets.QPushButton(GUI)
        self.btn_save.setGeometry(QtCore.QRect(70, 380, 131, 28))
        self.btn_save.setObjectName("btn_save")
        self.btn_edit = QtWidgets.QPushButton(GUI)
        self.btn_edit.setGeometry(QtCore.QRect(300, 380, 131, 28))
        self.btn_edit.setObjectName("btn_edit")
        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "GUI"))
        self.phoneNumber.setPlaceholderText(_translate("GUI", "   Phone Number"))
        self.message.setPlaceholderText(_translate("GUI", "   Message"))
        self.label.setText(_translate("GUI", "User Datas"))
        self.minute.setPlaceholderText(_translate("GUI", "   Minute"))
        self.label_2.setText(_translate("GUI", "Scheduling Datas"))
        self.hour.setPlaceholderText(_translate("GUI", "   Hour"))
        self.btn_save.setText(_translate("GUI", "Save"))
        self.btn_edit.setText(_translate("GUI", "Edit"))