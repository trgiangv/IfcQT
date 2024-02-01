from PySide6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setCentralWidget(QtWidgets.QLabel("Hello World"))
        self.show()


app = QtWidgets.QApplication([])
window = MainWindow()
app.exec()
