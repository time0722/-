import sys
from PyQt5.QtWidgets import QApplication
from mainwindow_refece import MainWindow_Event

app = QApplication(sys.argv)
ui = MainWindow_Event()
ui.show()
sys.exit(app.exec_())