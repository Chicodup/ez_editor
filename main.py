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
        self.ui.add_btn.clicked.connect(self.add_tag)
        self.ui.unpin_btn.clicked.connect(self.del_tag)
        self.ui.search_btn.clicked.connect(self.search_by_tag)




    def show_note(self):
        self.name = self.ui.list_btn.selectedItems()[0].text()
        self.ui.title_edit.setText(self.name)
        self.ui.text_edit.setText(self.notes[self.name]["текст"])

    def save_notes(self):
        tags = []
        for i in range(self.ui.list_btn_2.count()):
            tags.append(self.ui.list_btn_2.item(i).text())
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
    def add_tag(self):
        tag_name = self.ui.lineEdit_2.text()
        if tag_name !="":
            if tag_name not in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].append(tag_name)
                self.ui.list_btn_2.clear()
                self.ui.list_btn_2.addItems(self.notes[self.name]["теги"])

    def del_tag(self):
        if self.ui.list_btn_2.selectedItems():
            tag_name = self.ui.list_btn_2.selectedItems()[0].text()
            if tag_name not in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].remove(tag_name)
                self.ui.list_btn_2.clear()
                self.ui.list_btn_2.addItems(self.notes[self.name]["теги"])
    def search_by_tag(self):

        tag = self.ui.tag_edit.text()
        if tag:
            matching_notes = []
            for note_name in self.notes:
                if tag in self.notes[note_name]["теги"]:
                    matching_notes.append(note_name)
            self.ui.notes_list.clear()
            self.ui.notes_list.addItems(matching_notes)
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()