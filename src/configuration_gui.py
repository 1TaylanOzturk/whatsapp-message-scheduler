# File Binding
from UIs.design_of_configuration_window import UI as DesignOfConfigurationGUI
from UIs.design_of_editing_window import UI as DesignOfEditingWindow
# Modules
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import json


def write_to_json(data):
    with open("src/.config/targets.json", "r") as file:
        file_content = json.load(file)

    with open("src/.config/targets.json", "w") as file:
        file_content.append(data)
        file.write(json.dumps(file_content, indent=4))


class WindowOfEditing(QWidget, DesignOfEditingWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_save.clicked.connect(self.saveFile)
        self.btn_reset.clicked.connect(self.resetFile)
        with open("src/.config/targets.json", "r") as file:
            content = file.read()
        self.plainTextEdit.setPlainText(content)

    def saveFile(self):
        with open("src/.config/targets.json", "w") as file:
            file.write(self.plainTextEdit.toPlainText())

    def resetFile(self):
        self.plainTextEdit.setPlainText("[\n\n]")


class MainGUI(QWidget, DesignOfConfigurationGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_save.clicked.connect(self.save)
        self.btn_edit.clicked.connect(self.edit)

    def save(self):
        phone_num = self.phoneNumber.text()
        msg = self.message.toPlainText()
        hour = self.hour.text()
        minute = self.minute.text()
        data = {
            "target": phone_num,
            "message": msg,
            "hour": hour,
            "minute": minute
        }

        write_to_json(data)

    def edit(self):
        self.w = WindowOfEditing()
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())
