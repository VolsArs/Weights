import ap
import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QThread
import serial
import requests
import time
import logging
import pyperclip


class MyApp(QtWidgets.QMainWindow, ap.UIMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.windowSettings = None
        self.readingThread = ReadingTread()
        self.checkBox.stateChanged.connect(self.enable_settings)

        self.com_box.currentTextChanged.connect(self.comm_port_name_change)
        self.baud_box.currentTextChanged.connect(self.baud_rate_change)
        self.parity_box.currentTextChanged.connect(self.parity_change)
        self.data_byte_box.currentTextChanged.connect(self.date_byte_change)
        self.stop_bit_box.currentTextChanged.connect(self.stop_bit_change)

        self.com_box.setEnabled(False)
        self.baud_box.setEnabled(False)
        self.parity_box.setEnabled(False)
        self.data_byte_box.setEnabled(False)
        self.stop_bit_box.setEnabled(False)

        self.startReading_button.clicked.connect(self.start_read)
        self.null_button.clicked.connect(self.null_set)
        self.stop_button.clicked.connect(self.stop_read)
        self.copy_button.clicked.connect(self.copy_to_buffer)

    def on_change(self, s):
        self.lcdNumber.display(s)

    def start_read(self):
        if not self.readingThread.isRunning():
            self.readingThread.sig.connect(self.on_change)
            self.readingThread.running = True
            self.readingThread.start()
            logging.info("Пользователь запустил взвешивание")

    def stop_read(self):
        if self.readingThread.isRunning():
            self.readingThread.disconnect()
            self.readingThread.running = False
            logging.info("Пользователь остановил взвешивание")
        self.lcdNumber.display('off')

    def comm_port_name_change(self):
        self.readingThread.comm_name = self.com_box.currentText()

    def baud_rate_change(self):
        self.readingThread.baud_rate = int(self.baud_box.currentText())

    def parity_change(self):
        if self.parity_box.currentText() == 'None':
            self.readingThread.parity = serial.PARITY_NONE
        elif self.parity_box.currentText() == 'ODD':
            self.readingThread.parity = serial.PARITY_ODD
        elif self.parity_box.currentText() == 'EVEN':
            self.readingThread.parity = serial.PARITY_EVEN

    def date_byte_change(self):
        if self.data_byte_box.currentText() == '8':
            self.readingThread.byte_size = serial.EIGHTBITS
        elif self.data_byte_box.currentText() == '7':
            self.readingThread.byte_size = serial.SEVENBITS
        elif self.data_byte_box.currentText() == '6':
            self.readingThread.byte_size = serial.SIXBITS
        elif self.data_byte_box.currentText() == '5':
            self.readingThread.byte_size = serial.FIVEBITS

    def stop_bit_change(self):
        if self.stop_bit_box.currentText() == '1':
            self.readingThread.stop_bits = serial.STOPBITS_ONE
        elif self.stop_bit_box.currentText() == '2':
            self.readingThread.stop_bits = serial.STOPBITS_TWO

    def enable_settings(self):
        if not self.checkBox.isChecked():
            self.com_box.setEnabled(False)
            self.baud_box.setEnabled(False)
            self.parity_box.setEnabled(False)
            self.data_byte_box.setEnabled(False)
            self.stop_bit_box.setEnabled(False)
        else:
            self.com_box.setEnabled(True)
            self.baud_box.setEnabled(True)
            self.parity_box.setEnabled(True)
            self.data_byte_box.setEnabled(True)
            self.stop_bit_box.setEnabled(True)

    def null_set(self):
        requests.get('http://' + self.readingThread.ip_address + '/state.xml?relay1State=2')
        logging.info("Пользователь обнулил показания весов")

    def copy_to_buffer(self):
        if self.readingThread.isRunning():
            copying_weight = self.readingThread.weight
            pyperclip.copy(copying_weight)
            logging.info("Пользователь скопировал значение '" + copying_weight + "'")


class ReadingTread(QtCore.QThread):
    sig = QtCore.pyqtSignal(str)
    change_comport = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        # 192.168.2.20
        self.ip_address = '10.41.236.115'
        self.weight = '0'
        self.running = False
        self.comm_name = 'COM1'
        self.baud_rate = 9600
        self.byte_size = serial.EIGHTBITS
        self.parity = serial.PARITY_ODD
        self.stop_bits = serial.STOPBITS_ONE

    def run(self):
        port = serial.Serial()
        port.port = self.comm_name
        port.baudrate = self.baud_rate
        port.bytesize = self.byte_size
        port.parity = self.parity
        port.stopbits = self.stop_bits
        port.timeout = 1
        port.xonxoff = False
        port.rtscts = True
        port.dsrdtr = False

        try:
            port.open()
            port.reset_input_buffer()
            port.reset_output_buffer()
        except Exception as e:
            logging.exception(e)
            self.running = False
            self.sig.emit('error')

        line = 'X1'
        while self.running:
            try:
                port.write(line.encode('ascii'))
                time.sleep(1)
                read_bytes = port.read(14)
                current_line = read_bytes.decode('utf-8')[1:9].replace(' ', '')
                float(current_line)
                self.weight = current_line
                self.sig.emit(self.weight)
                requests.get('http://' + self.ip_address + '/state.xml?extvar1=' + self.weight)
                time.sleep(2)

            except Exception as e1:
                logging.exception(e1)

        port.close()
        requests.get('http://' + self.ip_address + '/state.xml?extvar1=0')
        requests.get('http://' + self.ip_address + '/state.xml?extvar0=0')
        requests.get('http://' + self.ip_address + '/state.xml?extvar2=0')


def main():
    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="terminal_log.log",
        filemode='a',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # Create app
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.setWindowTitle('Весовой терминал v1.3.5')
    app.exec()


if __name__ == '__main__':
    main()
