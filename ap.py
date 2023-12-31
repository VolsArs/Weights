# Form implementation generated from reading ui file 'C:/Users/AVolskiy/PycharmProjects/ap.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class UIMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(417, 229)
        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 10, 81, 16))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(9, 40, 271, 51))
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display('off')
        self.startReading_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startReading_button.setGeometry(QtCore.QRect(10, 100, 75, 23))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.startReading_button.sizePolicy().hasHeightForWidth())
        self.startReading_button.setSizePolicy(size_policy)
        self.startReading_button.setMinimumSize(QtCore.QSize(5, 0))
        self.startReading_button.setIconSize(QtCore.QSize(16, 16))
        self.startReading_button.setObjectName("startReading_button")
        self.stop_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(90, 100, 75, 23))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(size_policy)
        self.stop_button.setObjectName("stop_button")
        self.port_label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.port_label_2.setGeometry(QtCore.QRect(90, 150, 61, 16))
        self.port_label_2.setObjectName("port_label_2")
        self.com_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.com_box.setGeometry(QtCore.QRect(10, 170, 69, 22))
        self.com_box.setObjectName("com_box")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.com_box.addItem("")
        self.port_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.port_label.setGeometry(QtCore.QRect(10, 150, 51, 16))
        self.port_label.setObjectName("port_label")
        self.baud_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.baud_box.setGeometry(QtCore.QRect(90, 170, 69, 22))
        self.baud_box.setObjectName("baud_box")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.port_label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.port_label_3.setGeometry(QtCore.QRect(170, 150, 61, 16))
        self.port_label_3.setObjectName("port_label_3")
        self.parity_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.parity_box.setGeometry(QtCore.QRect(170, 170, 69, 22))
        self.parity_box.setObjectName("parity_box")
        self.parity_box.addItem("")
        self.parity_box.addItem("")
        self.parity_box.addItem("")
        self.port_label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.port_label_4.setGeometry(QtCore.QRect(250, 150, 61, 16))
        self.port_label_4.setObjectName("port_label_4")
        self.data_byte_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.data_byte_box.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.data_byte_box.setObjectName("data_byte_box")
        self.data_byte_box.addItem("")
        self.data_byte_box.addItem("")
        self.data_byte_box.addItem("")
        self.data_byte_box.addItem("")
        self.stop_bit_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.stop_bit_box.setGeometry(QtCore.QRect(330, 170, 69, 22))
        self.stop_bit_box.setObjectName("stop_bit_box")
        self.stop_bit_box.addItem("")
        self.stop_bit_box.addItem("")
        self.port_label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.port_label_5.setGeometry(QtCore.QRect(330, 150, 61, 16))
        self.port_label_5.setObjectName("port_label_5")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 0, 81, 16))
        self.checkBox.setObjectName("checkBox")
        self.null_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.null_button.setGeometry(QtCore.QRect(290, 60, 101, 31))
        self.null_button.setObjectName("null_button")
        #
        self.copy_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(191, 100, 90, 44))
        self.copy_button.setObjectName("copy_button")
        self.copy_button.setStyleSheet("background-color: orange")
        #
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Текущий вес"))
        self.startReading_button.setText(_translate("MainWindow", "Старт"))
        self.stop_button.setText(_translate("MainWindow", "Стоп"))
        self.port_label_2.setText(_translate("MainWindow", "Baud rate"))
        self.com_box.setItemText(0, _translate("MainWindow", "COM1"))
        self.com_box.setItemText(1, _translate("MainWindow", "COM2"))
        self.com_box.setItemText(2, _translate("MainWindow", "COM3"))
        self.com_box.setItemText(3, _translate("MainWindow", "COM4"))
        self.com_box.setItemText(4, _translate("MainWindow", "COM5"))
        self.com_box.setItemText(5, _translate("MainWindow", "COM6"))
        self.com_box.setItemText(6, _translate("MainWindow", "COM7"))
        self.com_box.setItemText(7, _translate("MainWindow", "COM8"))
        self.com_box.setItemText(8, _translate("MainWindow", "COM9"))
        self.com_box.setItemText(9, _translate("MainWindow", "COM10"))
        self.port_label.setText(_translate("MainWindow", "Com port"))
        self.baud_box.setItemText(0, _translate("MainWindow", "9600"))
        self.baud_box.setItemText(1, _translate("MainWindow", "4800"))
        self.baud_box.setItemText(2, _translate("MainWindow", "2400"))
        self.baud_box.setItemText(3, _translate("MainWindow", "1200"))
        self.baud_box.setItemText(4, _translate("MainWindow", "600"))
        self.port_label_3.setText(_translate("MainWindow", "Parity"))
        self.parity_box.setItemText(0, _translate("MainWindow", "ODD"))
        self.parity_box.setItemText(1, _translate("MainWindow", "EVEN"))
        self.parity_box.setItemText(2, _translate("MainWindow", "None"))
        self.port_label_4.setText(_translate("MainWindow", "Data bits"))
        self.data_byte_box.setItemText(0, _translate("MainWindow", "8"))
        self.data_byte_box.setItemText(1, _translate("MainWindow", "7"))
        self.data_byte_box.setItemText(2, _translate("MainWindow", "6"))
        self.data_byte_box.setItemText(3, _translate("MainWindow", "5"))
        self.stop_bit_box.setItemText(0, _translate("MainWindow", "1"))
        self.stop_bit_box.setItemText(1, _translate("MainWindow", "2"))
        self.port_label_5.setText(_translate("MainWindow", "Stop bits"))
        self.checkBox.setText(_translate("MainWindow", "Настроить"))
        self.null_button.setText(_translate("MainWindow", "Обнулить"))
        #
        self.copy_button.setText(_translate("MainWindow", "Копировать\r\nв буфер"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
