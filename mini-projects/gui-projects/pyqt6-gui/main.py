
# Dastur
# 1 - malumot qabul qiladi
# 2 - qayta ishlaydi
# 3 - natijani qaytaradi

# Intel(R) Core(TM) i3-8100 CPU @ 3.60GHz   3.60 GHz
# RAM DDR4 - DDR5 >> 2gb , 4gb , 8bg 16...32 , 64gb
# M2, SSD , HDD
#  M2 ~~ 100mbs
#  SSD ~~ 80mbs
#  HDD ~~ 30 mbs

# t.me/djangorobocode












import sys


from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


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

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        combo = QComboBox()
        for i in range(5):
            combo.addItem(f"Item {i}")
        print(combo.currentData())
        print(combo.currentText())
        print(combo)
        # for i in dir(combo):
            # with open("comboBox_methods.txt", "a") as file:
            #     file.write(f"{i}\n")

        layout.addWidget(combo)
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]
        #
        # for w in widgets:
        #     print(w.__str__(w))
        #     layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Устанавливаем центральный виджет окна. Виджет будет расширяться по умолчанию,
        # заполняя всё пространство окна.
        self.setCentralWidget(widget)



# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.label = QLabel("Click in this window")
#         self.setCentralWidget(self.label)
#
#     def mouseMoveEvent(self, e):
#         self.label.setText("mouseMoveEvent")
#
#     def mousePressEvent(self, e):
#         self.label.setText("mousePressEvent")
#
#     def mouseReleaseEvent(self, e):
#         self.label.setText("mouseReleaseEvent")
#
#     def mouseDoubleClickEvent(self, e):
#         self.label.setText("mouseDoubleClickEvent")


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




