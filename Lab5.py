import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QMessageBox, QLabel, QLineEdit, QAction, QComboBox, QFileDialog, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        btn = QPushButton('    Рассчетать    ', self)
        btn.move(285,128)
        self.resize(300, 150)
        
        btn1 = QPushButton("    Сохранить    ", self)
        btn.resize(btn.sizeHint())
        btn1.move(540, 128)
        btn1.clicked.connect(self.saveFileDialog)
        self.resize(300, 150)

        lbl = QLabel('Месяц:', self)
        lbl.move(5, 128)
 
        self.lbl = QLabel("Месяц")

        combo = QComboBox(self)
        combo.addItems(["Январь", "Февраль", "Март", "Апрель",
                        "Май", "Июнь", "Июль", "Август",
                        "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])

        combo.move(65, 128)
        
        combo.activated[str].connect(self.onActivated)

        lbl = QLabel('Имя:', self)
        lbl.move(5, 5)
        line = QLineEdit(self)
        line.move(65, 5)

        lbl = QLabel('Фамилия:', self)
        lbl.move(205, 5)
        line = QLineEdit(self)
        line.move(284, 5)

        lbl = QLabel('Должность:', self)
        lbl.move(425, 5)
        line = QLineEdit(self)
        line.move(492, 5)

        lbl = QLabel('Выработка:', self)
        lbl.move(5, 45)
        line = QLineEdit(self)
        line.move(65, 45)

        lbl = QLabel('Сверхурочные:', self)
        lbl.move(205, 45)
        line = QLineEdit(self)
        line.move(284, 45)

        lbl = QLabel('Штраф:', self)
        lbl.move(425, 45)
        line = QLineEdit(self)
        line.move(492, 45)

        lbl = QLabel('Оклад:', self)
        lbl.move(5, 85)
        line = QLineEdit(self)
        line.move(65, 85)

        lbl = QLabel('Премия:', self)
        lbl.move(205, 85)
        line = QLineEdit(self)
        line.move(284, 85)

        lbl = QLabel('Мат.помощь:', self)
        lbl.move(425, 85)
        line = QLineEdit(self)
        line.move(492, 85)


        self.setGeometry(800, 400, 640, 160)
        self.setWindowTitle('Зарплата')
        self.show()

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