import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from typing import Union, Optional
from operator import add, sub, mul, truediv


class mWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc_beaut.ui", self)

        self.operations = {
            '+': add,
            '-': sub,
            'x': mul,
            '/': truediv
        }

        self.b0.clicked.connect(lambda: self.add_digit('0'))
        self.b1.clicked.connect(lambda: self.add_digit('1'))
        self.b2.clicked.connect(lambda: self.add_digit('2'))
        self.b3.clicked.connect(lambda: self.add_digit('3'))
        self.b4.clicked.connect(lambda: self.add_digit('4'))
        self.b5.clicked.connect(lambda: self.add_digit('5'))
        self.b6.clicked.connect(lambda: self.add_digit('6'))
        self.b7.clicked.connect(lambda: self.add_digit('7'))
        self.b8.clicked.connect(lambda: self.add_digit('8'))
        self.b9.clicked.connect(lambda: self.add_digit('9'))

        self.bCE.clicked.connect(self.clear_all)
        self.bC.clicked.connect(self.clear_all)

        self.bdot.clicked.connect(self.add_point)

        self.bplus.clicked.connect(self.math_operation)
        self.bminus.clicked.connect(self.math_operation)
        self.bdiv.clicked.connect(self.math_operation)
        self.bmult.clicked.connect(self.math_operation)

        self.bequal.clicked.connect(self.calculate)

        self.bDELETE.clicked.connect(self.backspace)

    def add_digit(self, txt: str):
        if self.lineEdit.text() == '0':
            self.lineEdit.setText(txt)
        else:
            self.lineEdit.setText(self.lineEdit.text() + txt)

    def clear_all(self):
        self.lineEdit.setText('0')

    def add_point(self):
        if '.' not in self.lineEdit.text():
            self.lineEdit.setText(self.lineEdit.text() + '.')

    def add_temp(self):
        btn = self.sender()
        entry = self.lineEdit.text()

        if not self.lineUp.text() or self.get_math_sign() == '=':
            self.lineUp.setText(entry + f' {btn.text()} ')
            self.lineEdit.setText('0')

    def get_entry_num(self):
        entry = self.lineEdit.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self):
        if self.lineUp.text():
            temp = self.lineUp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self):
        if self.lineUp.text():
            return self.lineUp.text().strip('.').split()[-1]

    def calculate(self, flag=False):
        entry = self.lineEdit.text()
        temp = self.lineUp.text()

        if temp:
            res = self.operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num())
            print('res = ' + str(res))

            if not flag:
                self.lineUp.setText(temp + entry)
                self.lineEdit.setText(str(res))
            else:
                self.lineUp.setText(str(res))
                self.lineEdit.setText('0')
            return str(res)

    def math_operation(self) -> None:
        temp = self.lineUp.text()
        btn = self.sender()

        print('temp = ' + temp + ', btn=' + btn.text())

        if not temp:
            self.add_temp()
        else:
            print('math sign=' + self.get_math_sign() + ', btn = ' + btn.text())
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.lineUp.setText(self.calculate(True) + f' {btn.text()} ')
            else:
                self.lineUp.setText(self.calculate(True) + f' {btn.text()} ')
                self.lineEdit.setText('0')

    def backspace(self):
        entry = self.lineEdit.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.lineEdit.setText('0')
            else:
                self.lineEdit.setText(entry[:-1])
        else:
            self.lineEdit.setText('0')


app = QApplication(sys.argv)
ex = mWidget()
ex.show()
sys.exit(app.exec_())
