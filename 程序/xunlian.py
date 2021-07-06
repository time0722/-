# -*- coding: utf-8 -*-

'''
    本节主要实现主界面的GUI界面
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 490)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(680, 490))
        MainWindow.setMaximumSize(QtCore.QSize(680, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cartoon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.inputFile_label = QtWidgets.QLabel(self.centralwidget)
        self.inputFile_label.setGeometry(QtCore.QRect(30, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.inputFile_label.setFont(font)
        self.inputFile_label.setObjectName("inputFile_label")

        self.inputFile_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFile_edit.setGeometry(QtCore.QRect(100, 20, 141, 20))
        self.inputFile_edit.setObjectName("inputFile_edit")
        self.inputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.inputFile_btn.setGeometry(QtCore.QRect(250, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.inputFile_btn.setFont(font)
        self.inputFile_btn.setObjectName("inputFile_btn")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于最小方差组合模型的风电功率超短期预测"))
        self.inputFile_label.setText(_translate("MainWindow", "打开文件"))
        self.inputFile_btn.setText(_translate("MainWindow", "打开文件"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
