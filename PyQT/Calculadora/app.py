import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit, QSizePolicy




class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400,400)
        self.cw = QWidget()
        
        self.grid = QGridLayout(self.cw)

    #display
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0 , 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background: #fff;color:#000;font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        #adicionando botões na interface
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        
        
        #CLEAR
        self.add_btn(QPushButton('C'), 1, 4, 1, 1,
                     lambda: self.display.setText(''),
                     #style
                     'background:red;')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        
        
        self.add_btn(QPushButton('<-'), 2, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]),
                     'background:green;')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton('?'), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton('3'), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(QPushButton('='), 4, 4, 1, 1,
            self.eval_igual)


        self.setCentralWidget(self.cw)
   
   
    #Class buttons
    def add_btn(self, btn, row , col , rowspan , colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
            ))
        else:
            btn.clicked.connect(funcao)
        
        if style:
            btn.setStyleSheet(style)


        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    
    def eval_igual(self):
        try:
            self.display.setText(str
            (eval(self.display.text())))
        except Excepcion as e:
            self.display.setText("Conta invalida")



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()