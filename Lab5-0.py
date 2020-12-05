import sys
from PyQt5.QtWidgets import (QMainWindow, QToolTip, QPushButton, QMessageBox, QAction,  QLabel, QLineEdit, QComboBox, QFileDialog, QApplication)
# from PyQt5.QtGui import QFont

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        # saveAction = QAction('&Save', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.triggered.connect(qApp.quit)

        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(saveAction)

        # QToolTip.setFont(QFont('SansSerif', 10))
        btn = QPushButton('Рассчетать', self)
        # btn.setToolTip('Расчет зарплаты')
        # btn.resize(btn.sizeHint())
        btn.move(185,128)
        self.resize(250, 150)
        
        btn1 = QPushButton("Сохранить", self)
        # btn.resize(btn.sizeHint())
        btn1.move(335, 128)
        btn1.clicked.connect(self.saveFileDialog)
        # self.resize(250, 150)

        lbl = QLabel('Месяц:', self)
        lbl.move(1, 128)
 
        self.lbl = QLabel("Месяц")

        combo = QComboBox(self)
        combo.addItems(["Январь", "Февраль", "Март", "Апрель",
                        "Май", "Июнь", "Июль", "Август",
                        "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])

        combo.move(35, 128)
        
        combo.activated[str].connect(self.onActivated)

        lbl = QLabel('Имя:', self)
        lbl.move(5, 5)
        line = QLineEdit(self)
        line.move(35, 5)

        lbl = QLabel('Фамилия:', self)
        lbl.move(140, 5)
        line = QLineEdit(self)
        line.move(185, 5)

        lbl = QLabel('Профессия:', self)
        lbl.move(311, 5)
        line = QLineEdit(self)
        line.move(336, 5)

        lbl = QLabel('Раб:', self)
        lbl.move(5, 45)
        line = QLineEdit(self)
        line.move(35, 45)

        lbl = QLabel('After:', self)
        lbl.move(157, 45)
        line = QLineEdit(self)
        line.move(185, 45)

        lbl = QLabel('Fine:', self)
        lbl.move(311, 45)
        line = QLineEdit(self)
        line.move(336, 45)

        lbl = QLabel('Oklad:', self)
        lbl.move(5, 85)
        line = QLineEdit(self)
        line.move(35, 85)

        lbl = QLabel('Premium:', self)
        lbl.move(142, 85)
        line = QLineEdit(self)
        line.move(185, 85)

        lbl = QLabel('Material:', self)
        lbl.move(295, 85)
        line = QLineEdit(self)
        line.move(336, 85)


        self.setGeometry(820, 400, 450, 170)
        self.setWindowTitle('Зарплата')
        # s
        self.show()
        # self.saveFileDialog()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Вы уверены?",QMessageBox.Yes  |
            QMessageBox.No, QMessageBox.No)
        if  reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()
    
    def saveFileDialog(self, event):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())