import sys
#import serial
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QComboBox, QLabel, QGridLayout, QPlainTextEdit, QPushButton, QMessageBox, QMainWindow, \
    QApplication, QFileDialog


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.timer = QTimer(self)
        self.textArea = QPlainTextEdit()
        self.textArea.setReadOnly(True)
        # self.textArea.setStyleSheet("border: 3px solid red; background-color: black; color: white")
        self.textArea.setStyleSheet("border: 3px solid red; background-color: black; background-image: url(grey.png)")
        self.textArea.setFont(QtGui.QFont('Courier', 15))
        self.lab1 = QLabel('Kolejne czynności' + '\n' + '\n' + 'Ustaw parametry portu')
        self.lab3 = QLabel('Pobierz dane z portu')
        self.lab4 = QLabel('Zapisz plik na dysk')
        self.lab5 = QLabel('Wyczyść konsolę')
        self.lab1.setMaximumWidth(230)
        self.lab3.setMaximumWidth(230)
        self.lab4.setMaximumWidth(230)
        self.lab5.setMaximumWidth(230)
        self.lab3.setWordWrap(True)
        self.lab1.setFont(QtGui.QFont('Courier', 13))
        self.lab3.setFont(QtGui.QFont('Courier', 13))
        self.lab4.setFont(QtGui.QFont('Courier', 13))
        self.lab5.setFont(QtGui.QFont('Courier', 13))
        myFont = QtGui.QFont('Courier', 10)
        myFont.setBold(True)
        self.lab6 = QLabel('Ustawienia')
        self.lab6.setMaximumHeight(50)
        self.lab7 = QLabel(':Comm Port')
        self.lab8 = QLabel(':Baud Rate')
        self.lab9 = QLabel(':Stop Bits')
        self.lab10 = QLabel(':Data Bits')
        self.lab11 = QLabel(':Parity')
        self.lab12 = QLabel(':Time')
        self.lab13 = QLabel(':Xon/Xoff')
        self.lab14 = QLabel(':Rts/Cts')
        self.lab6.setFont(QtGui.QFont('Courier', 13))
        self.lab7.setFont(QtGui.QFont('Courier', 10))
        self.lab8.setFont(QtGui.QFont('Courier', 10))
        self.lab9.setFont(QtGui.QFont('Courier', 10))
        self.lab10.setFont(QtGui.QFont('Courier', 10))
        self.lab11.setFont(QtGui.QFont('Courier', 10))
        self.lab12.setFont(QtGui.QFont('Courier', 10))
        self.lab13.setFont(QtGui.QFont('Courier', 10))
        self.lab14.setFont(QtGui.QFont('Courier', 10))
        self.comb7 = QComboBox()
        self.comb8 = QComboBox()
        self.comb9 = QComboBox()
        self.comb10 = QComboBox()
        self.comb11 = QComboBox()
        self.comb12 = QComboBox()
        self.comb13 = QComboBox()
        self.comb14 = QComboBox()
        self.comb7.setFont(QtGui.QFont('Courier', 10))
        self.comb8.setFont(QtGui.QFont('Courier', 10))
        self.comb9.setFont(QtGui.QFont('Courier', 10))
        self.comb10.setFont(QtGui.QFont('Courier', 10))
        self.comb11.setFont(QtGui.QFont('Courier', 10))
        self.comb12.setFont(QtGui.QFont('Courier', 10))
        self.comb13.setFont(QtGui.QFont('Courier', 10))
        self.comb14.setFont(QtGui.QFont('Courier', 10))
        list7 = ['COM4', 'COM1', 'COM2', 'COM3']
        list8 = ['1200', '2400', '4800', '9600', '14400', '19200', '38400', '56000']
        list9 = ['1', '1.5', '2']
        list10 = ['5', '6', '7', '8']
        list11 = ["None", "Odd", "Even", "Mark", "Space"]
        list12 = ["Limited", "Infinite"]
        list13 = ["Off", 'On']
        self.comb7.addItems(list7)
        self.comb8.addItems(list8)
        self.comb9.addItems(list9)
        self.comb10.addItems(list10)
        self.comb11.addItems(list11)
        self.comb12.addItems(list12)
        self.comb13.addItems(list13)
        self.comb14.addItems(list13)
        load_btn = QPushButton('Ustaw port', self)
        count_btn = QPushButton('Pobierz dane', self)
        end_btn = QPushButton('&Koniec', self)
        save_btn = QPushButton('Zapisz dane', self)
        clear_btn = QPushButton('Wyczyść', self)
        end_btn.resize(end_btn.sizeHint())
        load_btn.setMaximumWidth(245)
        count_btn.setMaximumWidth(245)
        save_btn.setMaximumWidth(245)
        clear_btn.setMaximumWidth(245)
        end_btn.setMaximumWidth(245)
        load_btn.setFont(QtGui.QFont('Courier', 13))
        count_btn.setFont(QtGui.QFont('Courier', 13))
        save_btn.setFont(QtGui.QFont('Courier', 13))
        clear_btn.setFont(QtGui.QFont('Courier', 13))
        end_btn.setFont(QtGui.QFont('Courier', 13))
        load_btn.setStyleSheet('QPushButton { background-color: red; color: white; font: bold}'
                               'QPushButton:pressed { background-color: black}')
        count_btn.setStyleSheet('QPushButton { background-color: black; color: white; font: bold}'
                                'QPushButton:pressed { background-color: grey}')
        save_btn.setStyleSheet('QPushButton { background-color: red; color: white; font: bold}'
                              'QPushButton:pressed { background-color: black}')
        clear_btn.setStyleSheet('QPushButton { background-color: black; color: white; font: bold}'
                                 'QPushButton:pressed { background-color: grey}')
        end_btn.setStyleSheet('QPushButton { background-color: red; color: white; font: bold}'
                                'QPushButton:pressed { background-color: black}')
        layout = QGridLayout()
        layout.addWidget(self.lab1, 0, 3, 1, 2)
        layout.addWidget(self.lab3, 9, 3, 1, 2)
        layout.addWidget(self.lab4, 11, 3, 1, 2)
        layout.addWidget(self.lab5, 13, 3, 1, 2)
        layout.addWidget(self.lab7, 1, 4, 1, 1)
        layout.addWidget(self.lab8, 2, 4, 1, 1)
        layout.addWidget(self.lab9, 3, 4, 1, 1)
        layout.addWidget(self.lab10, 4, 4, 1, 1)
        layout.addWidget(self.lab11, 5, 4, 1, 1)
        layout.addWidget(self.lab12, 6, 4, 1, 1)
        layout.addWidget(self.lab13, 7, 4, 1, 1)
        layout.addWidget(self.lab14, 8, 4, 1, 1)
        layout.addWidget(self.comb7, 1, 3, 1, 1)
        layout.addWidget(self.comb8, 2, 3, 1, 1)
        layout.addWidget(self.comb9, 3, 3, 1, 1)
        layout.addWidget(self.comb10, 4, 3, 1, 1)
        layout.addWidget(self.comb11, 5, 3, 1, 1)
        layout.addWidget(self.comb12, 6, 3, 1, 1)
        layout.addWidget(self.comb13, 7, 3, 1, 1)
        layout.addWidget(self.comb14, 8, 3, 1, 1)
        layout.addWidget(end_btn, 15, 3, 1, 2)
        layout.addWidget(count_btn, 10, 3, 1, 2)
        layout.addWidget(save_btn, 12, 3, 1, 2)
        layout.addWidget(clear_btn, 14, 3, 1, 2)
        layout.addWidget(self.textArea, 0, 0, 16, 3)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        end_btn.clicked.connect(self.end)
        count_btn.clicked.connect(self.reading)
        save_btn.clicked.connect(self.save_file)
        clear_btn.clicked.connect(self.clear_wind)
        self.setGeometry(0, 0, 800, 600)
        self.setStyleSheet('background-color: white')
        self.setCentralWidget(widget)
        self.setWindowIcon(QIcon("pw.png"))
        self.setWindowTitle('Elektroniczna technika pomiarowa w geodezji')
        self.show()

    def end(self):
        self.close()

    def reading(self):
        self.textArea.appendPlainText('Trwa pobieranie danych...')
        self.update()
        port = str(self.comb7.currentText())
        baudrate = str(self.comb8.currentText())
        stop_bits = str(self.comb9.currentText())
        parity = str(self.comb11.currentText())
        data_bits = int(self.comb10.currentText())
        time2 = str(self.comb12.currentText())
        xonxoff = str(self.comb13.currentText())
        rtscts = str(self.comb14.currentText())
        if parity == "None":
            parity = "N"
        if time2 == "Limited":
            time2 = "1"
        if time2 == "Infinite":
            time2 = "0"
        if xonxoff == "Off":
            xonxoff = "0"
        if xonxoff == "On":
            xonxoff = "1"
        if rtscts == "Off":
            rtscts = "0"
        if rtscts == "On":
            rtscts = "1"
        # try:
        #     ser = serial.Serial(
        #         port=port, baudrate=baudrate, bytesize=data_bits, parity=parity, stopbits=int(stop_bits),
        #         timeout=int(time2), xonxoff=int(xonxoff), rtscts=int(rtscts))
        #
        #     if ser.isOpen():
        #         print(ser.name + ' is open')
        #
        #     while 1:
        #         line = ser.readline()
        #         self.textArea.appendPlainText(str(line))
        #         if len(line) == 0:
        #             break
        # except (ValueError, TypeError):
        #     QMessageBox.warning(self, 'Błąd!', '  Wprowadź poprawne dane!         ', QMessageBox.Ok)

    def closeEvent(self, event):
        odp = QMessageBox.question(
            self, 'Komunikat',
            'Czy na pewno chcesz zamknąć aplikację?    ',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def clear_wind(self):
        self.textArea.clear()

    def save_file(self):
        try:
            name = QFileDialog.getSaveFileName(self, '/', '.txt')[0]
            save = open(name, 'w')
            save.writelines(self.textArea.toPlainText())
            save.close()
        except FileNotFoundError:
            pass

app = QApplication(sys.argv)
w = MainWindow()
app.exec_()