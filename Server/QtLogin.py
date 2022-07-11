from PyQt5.QtWidgets import *
import sys

import login
import query


class Main(QDialog, login.Ui_MainWindow, query.Ui_Query_Main):
    def __init__(self):
        super(login.Ui_MainWindow, self).__init__()
        super().__init__()
        self.QWindow = None
        self.setupUi(self)
        self.Login.clicked.connect(self.Query)

    def Query(self):
        self.QWindow = QMainWindow()
        self.setupUi(self)


class QueryWindow(QDialog, query.Ui_Query_Main):
    def __init__(self):
        super(query.Ui_Query_Main, self).__init__()
        super().__init__()
        self.setupUi(self)


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
