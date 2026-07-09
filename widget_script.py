import sys
from sql import add_todo, get_todos
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget, QWidget, QVBoxLayout



# Subclass um das Appfenster zu gestalten 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input_field = QLineEdit()
        self.todo_list = QListWidget()
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.todo_list)
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setFixedSize(QSize(400, 200))
        self.input_field.returnPressed.connect(self.add_new_todo)
        self.refresh_list()

    def add_new_todo(self):
        text = self.input_field.text()
        if text.strip() == "":
            return
        add_todo(text)
        self.input_field.clear()
        self.refresh_list()

    def refresh_list(self):
        self.todo_list.clear()
        for row in get_todos():
            self.todo_list.addItem(row[1])

      


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
