import sys


from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

# window_titles = [
#     'My App',
#     'My App',
#     'Still My App',
#     'Still My App',
#     'What on earth',
#     'What on earth',
#     'This is surprising',
#     'This is surprising',
#     'Something went wrong'
# ]



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.n_times_clicked = 0
#
#         self.setWindowTitle("My App")
#
#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)
#
#         self.windowTitleChanged.connect(self.the_window_title_changed)
#
#         # Устанавливаем центральный виджет Window.
#         self.setCentralWidget(self.button)
#
#     def the_button_was_clicked(self):
#         print("Clicked.")
#         new_window_title = choice(window_titles)
#         print("Setting title:  %s" % new_window_title)
#         self.setWindowTitle(new_window_title)
#
#     def the_window_title_changed(self, window_title):
#         print("Window title changed: %s" % window_title)
#
#         if window_title == 'Something went wrong':
#             self.button.setDisabled(True)

