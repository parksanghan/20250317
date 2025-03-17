# 20250317

# Python 개발환경 정리 및 주소록 만들기

## 1. Python 및 VSCode 설치
- 기존 설치된 Anaconda, VSCode 제거 후 재설치
- Anaconda를 사용한 Python 설치 및 가상환경 설정

## 2. 가상환경 만들기 및 관리
```bash
conda create -n myenv01
conda create -n myenv02 python=3.9
```

## 3. VSCode 설정
- VSCode 설치 후 Python Extension 추가
- `Ctrl+Shift+P` 로 가상환경 연결

## 4. 주소록 프로그램 개발 (PyQt5 사용)
### 4.1. 프로젝트 폴더 생성
```bash
mkdir AddressBookProject
cd AddressBookProject
```

### 4.2. PyQt5 설치
```bash
pip install PyQt5
```

### 4.3. 주소록 프로그램 코드
```python
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QLineEdit, QFileDialog
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
```

## 5. 최종 실행 및 디버깅
```bash
python myFirstCode.py
```
- `F5` 또는 `Ctrl+F5` 로 프로그램 실행
