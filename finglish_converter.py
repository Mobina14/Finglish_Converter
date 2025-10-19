import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class FinglishConverter:
    def __init__(self):
        self.mistyped_map = {
            'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع',
            'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'چ', 'a': 'ش', 's': 'س',
            'd': 'ی', 'f': 'ب', 'g': 'ل', 'h': 'ا', 'j': 'ت', 'k': 'ن', 'l': 'م',
            ';': 'ک', "'": 'گ', 'z': 'ظ', 'x': 'ط', 'c': 'ز', 'v': 'ر', 'b': 'ذ',
            'n': 'د', 'm': 'پ', ',': 'و'
        }

    def convert_mistyped(self, text):
        result = ''
        for char in text.lower():
            result += self.mistyped_map.get(char, char)
        return result

    def convert_finglish(self, text):
        # Replace with your Google AI Studio API key
        API_KEY = "AIzaSyD8NtY0XqCi1blagFyUoWg8vDNJ2dUE8UQ"
        url = "https://aistudio.google.com/api/gemini"  # Update with correct endpoint
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {
            "prompt": f"Convert this Finglish text to Persian: {text}",
            "model": "gemini-pro"
        }
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json().get("converted_text", "خطا: تبدیل انجام نشد")
        except requests.RequestException as e:
            return f"خطا: درخواست API ناموفق بود - {str(e)}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("مبدل فینگلیش به فارسی")
        self.setGeometry(100, 100, 600, 400)
        
        self.converter = FinglishConverter()
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("اینجا متن فینگلیش یا بهم‌ریخته را وارد کنید...")
        layout.addWidget(QLabel("متن ورودی:"))
        layout.addWidget(self.input_text)
        
        button_layout = QHBoxLayout()
        self.finglish_button = QPushButton("تبدیل فینگلیش")
        self.mistyped_button = QPushButton("تبدیل متن بهم‌ریخته")
        self.finglish_button.clicked.connect(self.convert_finglish)
        self.mistyped_button.clicked.connect(self.convert_mistyped)
        button_layout.addWidget(self.finglish_button)
        button_layout.addWidget(self.mistyped_button)
        layout.addLayout(button_layout)
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(QLabel("متن خروجی:"))
        layout.addWidget(self.output_text)
        
        self.input_text.setLayoutDirection(Qt.RightToLeft)
        self.output_text.setLayoutDirection(Qt.RightToLeft)

    def convert_finglish(self):
        text = self.input_text.toPlainText()
        converted = self.converter.convert_finglish(text)
        self.output_text.setText(converted)

    def convert_mistyped(self):
        text = self.input_text.toPlainText()
        converted = self.converter.convert_mistyped(text)
        self.output_text.setText(converted)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())