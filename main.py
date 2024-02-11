from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

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
        self.ui.notes_list.addItems(self.notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
