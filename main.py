from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
from Ui import Ui_MainWindow
import random
import sys


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.can_paint = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.can_paint = True
        self.repaint()
        self.can_paint = False

    def paintEvent(self, event) -> None:
        if self.can_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QBrush(QColor(*(random.randint(0, 255) for _ in range(3)))))

            x, y = random.randint(0, self.width()), random.randint(0, self.height())
            w = random.randint(0, self.width())
            qp.drawEllipse(x, y, w, w)

            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_ = App()
    app_.show()
    sys.exit(app.exec_())
