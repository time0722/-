# -*- coding: utf-8 -*-

"""
    本节为主窗口的事件接口汇总
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from yunxing import yunxing_Model


class MainWindow_Event(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow_Event, self).__init__(parent)
        self.setupUi(self)

    # 打开文件按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):
        bigDataName, _ = QFileDialog.getOpenFileName(self, "打开一个文本文件", ".", "表格文件 (*.csv)")
        self.inputFile_edit.setText(bigDataName)

    # 开始计算按钮
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        filePath = self.inputFile_edit.text()
        if filePath[-4:] == ".csv":

            self.textEdit.clear()
            self.textEdit.insertPlainText("开始计算" + '-' * 15 + '\n')
            # 导入ARIMA模型
            self.YunXing_model = yunxing_Model(filePath)
            comments_clean, comment_cut, all_words, comment_cut_mumber, result, long = self.YunXing_model.yunxing()
            self.textEdit.inserPlainText('评价分割数量为：'+ str(comment_cut_mumber)+'\n')
            self.textEdit.inserPlainText('筛选后剩余数量为' + str(long) + '\n\n')
            self.textEdit.insertPlainText('评价分类结果（1为优点，0为缺点）' + str(result) + '\n\n')
        else:
            QMessageBox.warning(self, "文件类型错误", "选择的文件不是csv格式", QMessageBox.Yes, QMessageBox.Yes)