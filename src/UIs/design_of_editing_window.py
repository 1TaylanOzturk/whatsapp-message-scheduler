from PyQt5 import QtCore, QtWidgets


class UI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(400, 432)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(GUI)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 10, 401, 291))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btn_save = QtWidgets.QPushButton(GUI)
        self.btn_save.setGeometry(QtCore.QRect(150, 340, 90, 28))
        self.btn_save.setObjectName("btn_save")
        self.btn_reset = QtWidgets.QPushButton(GUI)
        self.btn_reset.setGeometry(QtCore.QRect(150, 380, 90, 28))

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "GUI"))
        self.btn_save.setText(_translate("GUI", "Save"))
        self.btn_reset.setText(_translate("GUI", "Reset"))
