import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class index_mainWindow(QMainWindow):
    def __init__(self):
        super(index_mainWindow, self).__init__()
        self.setWindowTitle('明日方舟寻访统计工具')  # 窗口标题
        self.setGeometry(5, 30, 1375, 750)  # 窗口的大小和位置设置
        self.browser = QWebEngineView()
        # 加载html代码(这里注意html代码是用三个单引号包围起来的)
        self.browser.load(QUrl(QFileInfo("./html/index.html").absoluteFilePath()))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = index_mainWindow()
    win.show()
    app.exit(app.exec_())
