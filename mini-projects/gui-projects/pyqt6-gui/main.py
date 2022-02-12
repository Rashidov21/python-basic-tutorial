from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

# window = QWidget()
window = QPushButton("Click me")
window.show()

app.exec()