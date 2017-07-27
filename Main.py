#! /usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow
from views import main
from views import cliente
class Principal(QApplication):
    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.window = QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == '__main__':
    import sys
    app = Principal(sys.argv)
    sys.exit(app.exec_())
