import sys
from PyQt5 import QtWidgets
from pic import Ui_Form
import win32ui
from PyQt5 import QtCore
import run_k_means
from PyQt5.QtWidgets import QMessageBox

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        self.colorcnt = 2  # 默认颜色数
        self.fi = ""  # 默认图片输入路径
        self.fo = ""  # 默认图片输出路径
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    def choosepic(self):
        dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        dlg.SetOFNInitialDir('C:')  # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()
        filename = dlg.GetPathName()  # 获取选择的文件名称
        self.fi = filename
        self.lineEdit.setText(filename)  # 将获取的文件名称写入名为“lineEdit_InputId_AI”可编辑文本框中

    def chooseout(self):
        dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        dlg.SetOFNInitialDir('C:')  # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()
        filename = dlg.GetPathName()  # 获取选择的文件名称
        self.fo = filename
        self.lineEdit_2.setText(filename)  # 将获取的文件名称写入名为“lineEdit_InputId_AI”可编辑文本框中

    def okb(self):
        self.colorcnt = self.lineEdit_3.text() # 获得文本内容
        print(self.colorcnt)

    def startp(self):
        print(self.lineEdit_3.text())
        if run_k_means.runsys(self.fi, self.lineEdit_3.text(), self.fo):
            QMessageBox().about(None, "提示", "运行成功！")
            sys.exit()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
