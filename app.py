
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QFileDialog
import sys

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('주소록')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["이름", "전화번호"])
        layout.addWidget(self.table)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("이름 입력")
        layout.addWidget(self.name_input)

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("전화번호 입력")
        layout.addWidget(self.phone_input)

        self.add_button = QPushButton("추가", self)
        self.add_button.clicked.connect(self.addEntry)
        layout.addWidget(self.add_button)

        self.save_button = QPushButton("저장", self)
        self.save_button.clicked.connect(self.saveToFile)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def addEntry(self):
        name = self.name_input.text()
        phone = self.phone_input.text()

        if name and phone:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(phone))

            self.name_input.clear()
            self.phone_input.clear()

    def saveToFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "저장할 파일 선택", "", "텍스트 파일 (*.txt);;모든 파일 (*)", options=options)
        
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                for row in range(self.table.rowCount()):
                    name = self.table.item(row, 0).text()
                    phone = self.table.item(row, 1).text()
                    file.write(f"{name},{phone}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AddressBook()
    ex.show()
    sys.exit(app.exec_())
