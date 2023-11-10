# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import main


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # Define a new Signal

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass  # This can remain empty


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(10, 10, 781, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.title_label.setFont(font)
        self.title_label.setScaledContents(True)
        self.title_label.setObjectName("title_label")
        self.channel_input = QtWidgets.QLineEdit(self.centralwidget)
        self.channel_input.setGeometry(QtCore.QRect(30, 150, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.channel_input.setFont(font)
        self.channel_input.setText("")
        self.channel_input.setObjectName("channel_input")
        self.output_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_textBrowser.setGeometry(QtCore.QRect(415, 150, 371, 401))
        self.output_textBrowser.setObjectName("output_textBrowser")
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(30, 480, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start_pushButton.setFont(font)
        self.start_pushButton.setObjectName("start_pushButton")
        self.start_pushButton.clicked.connect(self.run_main)
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(260, 480, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stop_pushButton.setFont(font)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.stop_pushButton.clicked.connect(self.terminate_process)
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(50, 340, 321, 131))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/image/colour_logo.png"))
        self.logo_label.setScaledContents(False)
        self.logo_label.setObjectName("logo_label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(420, 110, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_label.setFont(font)
        self.output_label.setObjectName("output_label")
        self.count_input = QtWidgets.QLineEdit(self.centralwidget)
        self.count_input.setGeometry(QtCore.QRect(30, 220, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.count_input.setFont(font)
        self.count_input.setText("")
        self.count_input.setObjectName("count_input")
        self.dir_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dir_input.setGeometry(QtCore.QRect(30, 290, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dir_input.setFont(font)
        self.dir_input.setText("")
        self.dir_input.setObjectName("dir_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.redirect_stdout_to_output()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Videos to Frames</span></p></body></html>"))
        self.channel_input.setPlaceholderText(_translate("MainWindow", "크리에이터 ID를 입력하세요"))
        self.start_pushButton.setText(_translate("MainWindow", "실행"))
        self.stop_pushButton.setText(_translate("MainWindow", "종료"))
        self.output_label.setText(_translate("MainWindow", "Console"))
        self.count_input.setPlaceholderText(_translate("MainWindow", "수집할 영상 갯수를 입력하세요"))
        self.dir_input.setPlaceholderText(_translate("MainWindow", "결과물을 저장할 경로를 입력하세요"))


    def redirect_stdout_to_output(self):
        # Redirect stdout to EmittingStream
        sys.stdout = EmittingStream(textWritten=self.append_to_output_text_browser)


    def append_to_output_text_browser(self, text):
        # Append text to the QTextBrowser
        self.output_textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.output_textBrowser.insertPlainText(text)

    def run_main(self):
        # 입력된 값 가져오기
        channel = self.channel_input.text()
        count = int(self.count_input.text())
        directory = self.dir_input.text()

        # main 모듈의 main 함수에 입력 값을 전달합니다.
        main.main(channel, count, directory)

    def terminate_process(self):
        quit()


import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    original_stdout = sys.stdout  # Save a reference to the original standard output


    def restore_stdout():
        sys.stdout = original_stdout


    app.aboutToQuit.connect(restore_stdout)  # Restore the original stdout when the app is about to quit

    sys.exit(app.exec_())
