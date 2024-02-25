import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import json
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {
            "перша замітка":{
                "текст": "Це текст першої замітки",
                "теги":[]
            }
        }
        self.ui.list_btn.addItems(self.notes)
        self.ui.list_btn.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_notes)
        self.ui.create_btn.clicked.connect(self.create_note)
        self.ui.delete_btn_2.clicked.connect(self.delete_note)


    def show_note(self):
        self.name = self.ui.list_btn.selectedItems()[0].text()
        self.ui.title_edit.setText(self.name)
        self.ui.text_edit.setText(self.notes[self.name]["текст"])

    def save_notes(self):
        self.notes[self.ui.title_edit.text()] = {
        "текст": self.ui.text_edit.toPlainText(),
        "теги": []
        }
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file)
        self.ui.list_btn.clear()
        self.ui.list_btn.addItems(self.notes)
    def clear(self):
        self.ui.title_edit.clear()
        self.ui.text_edit.clear()

    def create_note(self):
        self.clear()
    def read_notes(self):
        try:
            with open("notes.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                "перша замітка":{
                "текст": "Це текст першої замітки",
                "теги":[]
            }
            }
    def delete_note(self):
        # try:
            del self.notes[self.name]
            self.clear()
            self.ui.list_btn.clear()
            self.ui.list_btn.addItems(self.notes)
            self.save_notes()
        # except:
            # print("помилка видалення")
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
