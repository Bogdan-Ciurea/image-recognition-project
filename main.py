from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QWidget, QMainWindow
from PyQt5.uic import loadUi
import sys

from excel import getInfoFromExcel, changeData
from castel import atacCastel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('Assets/view.ui', self)
        self.pushButton.clicked.connect(self.beginAtack)

    # The main function of the class that activates of button press
    def beginAtack(self):
        self.castel = self.tabWidget.currentIndex() + 1
        numarDeAtacat, ordine = self.NumarTinte.value(), self.comboBox.currentIndex() + 1
        if self.castel == 1:
            n, a = self.listOfChecks_1()
        elif self.castel == 2:
            n, a = self.listOfChecks_2()
        elif self.castel == 3:
            n, a = self.listOfChecks_3()
        else:
            n, a = self.listOfChecks_4()
        
        targets = getInfoFromExcel(self.castel, numarDeAtacat, ordine, n, a)
        self.processList(targets)
 
    # The function that will atack an individual castle
    def processList(self, targets):
        for x, y, lvl, lvlToLvl in targets:
            #print(x, y, lvl, lvlToLvl)
            if atacCastel(x, y, lvl, lvlToLvl):
                changeData(self.castel, x, y)
    

    # checkBox management functions
    def listOfChecks_1(self):
        s = 0
        a = []
        if self.checkBox.isChecked() == True:
            s += 1
            a.append(1)
        if self.checkBox_2.isChecked() == True:
            s += 1
            a.append(2)
        if self.checkBox_3.isChecked() == True:
            s += 1
            a.append(3)
        if self.checkBox_4.isChecked() == True:
            s += 1
            a.append(4)
        if self.checkBox_5.isChecked() == True:
            s += 1
            a.append(5)
        if self.checkBox_6.isChecked() == True:
            s += 1
            a.append(6)
        if self.checkBox_7.isChecked() == True:
            s += 1
            a.append(7)
        if self.checkBox_8.isChecked() == True:
            s += 1
            a.append(8)
        if self.checkBox_9.isChecked() == True:
            s += 1
            a.append(9)
        if self.checkBox_10.isChecked() == True:
            s += 1
            a.append(10)
        if self.checkBox_11.isChecked() == True:
            s += 1
            a.append(11)
        if self.checkBox_12.isChecked() == True:
            s += 1
            a.append(12)
        if self.checkBox_13.isChecked() == True:
            s += 1
            a.append(13)
        if self.checkBox_14.isChecked() == True:
            s += 1
            a.append(14)
        if self.checkBox_15.isChecked() == True:
            s += 1
            a.append(15)
        if self.checkBox_16.isChecked() == True:
            s += 1
            a.append(16)
        if self.checkBox_17.isChecked() == True:
            s += 1
            a.append(17)
        if self.checkBox_18.isChecked() == True:
            s += 1
            a.append(18)
        if self.checkBox_19.isChecked() == True:
            s += 1
            a.append(19)
        if self.checkBox_20.isChecked() == True:
            s += 1
            a.append(20)
        if s == 0:
            a = [0]
        return s,a 

    def listOfChecks_2(self):
        s = 0
        a = []
        if self.checkBox_21.isChecked() == True:
            s += 1
            a.append(1)
        if self.checkBox_22.isChecked() == True:
            s += 1
            a.append(2)
        if self.checkBox_23.isChecked() == True:
            s += 1
            a.append(3)
        if self.checkBox_24.isChecked() == True:
            s += 1
            a.append(4)
        if self.checkBox_25.isChecked() == True:
            s += 1
            a.append(5)
        if self.checkBox_26.isChecked() == True:
            s += 1
            a.append(6)
        if self.checkBox_27.isChecked() == True:
            s += 1
            a.append(7)
        if self.checkBox_28.isChecked() == True:
            s += 1
            a.append(8)
        if self.checkBox_29.isChecked() == True:
            s += 1
            a.append(9)
        if self.checkBox_30.isChecked() == True:
            s += 1
            a.append(10)
        if self.checkBox_31.isChecked() == True:
            s += 1
            a.append(11)
        if self.checkBox_32.isChecked() == True:
            s += 1
            a.append(12)
        if self.checkBox_33.isChecked() == True:
            s += 1
            a.append(13)
        if self.checkBox_34.isChecked() == True:
            s += 1
            a.append(14)
        if self.checkBox_35.isChecked() == True:
            s += 1
            a.append(15)
        if self.checkBox_36.isChecked() == True:
            s += 1
            a.append(16)
        if self.checkBox_37.isChecked() == True:
            s += 1
            a.append(17)
        if self.checkBox_38.isChecked() == True:
            s += 1
            a.append(18)
        if self.checkBox_39.isChecked() == True:
            s += 1
            a.append(19)
        if self.checkBox_40.isChecked() == True:
            s += 1
            a.append(20)
        if s == 0:
            a = [0]
        return s,a

    def listOfChecks_3(self):
        s = 0
        a = []
        if self.checkBox_41.isChecked() == True:
            s += 1
            a.append(1)
        if self.checkBox_42.isChecked() == True:
            s += 1
            a.append(2)
        if self.checkBox_43.isChecked() == True:
            s += 1
            a.append(3)
        if self.checkBox_44.isChecked() == True:
            s += 1
            a.append(4)
        if self.checkBox_45.isChecked() == True:
            s += 1
            a.append(5)
        if self.checkBox_46.isChecked() == True:
            s += 1
            a.append(6)
        if self.checkBox_47.isChecked() == True:
            s += 1
            a.append(7)
        if self.checkBox_48.isChecked() == True:
            s += 1
            a.append(8)
        if self.checkBox_49.isChecked() == True:
            s += 1
            a.append(9)
        if self.checkBox_50.isChecked() == True:
            s += 1
            a.append(10)
        if self.checkBox_51.isChecked() == True:
            s += 1
            a.append(11)
        if self.checkBox_52.isChecked() == True:
            s += 1
            a.append(12)
        if self.checkBox_53.isChecked() == True:
            s += 1
            a.append(13)
        if self.checkBox_54.isChecked() == True:
            s += 1
            a.append(14)
        if self.checkBox_55.isChecked() == True:
            s += 1
            a.append(15)
        if self.checkBox_56.isChecked() == True:
            s += 1
            a.append(16)
        if self.checkBox_57.isChecked() == True:
            s += 1
            a.append(17)
        if self.checkBox_58.isChecked() == True:
            s += 1
            a.append(18)
        if self.checkBox_59.isChecked() == True:
            s += 1
            a.append(19)
        if self.checkBox_60.isChecked() == True:
            s += 1
            a.append(20)
        if s == 0:
            a = [0]
        return s,a

    def listOfChecks_4(self):
        s = 0
        a = []
        if self.checkBox_61.isChecked() == True:
            s += 1
            a.append(1)
        if self.checkBox_62.isChecked() == True:
            s += 1
            a.append(2)
        if self.checkBox_63.isChecked() == True:
            s += 1
            a.append(3)
        if self.checkBox_64.isChecked() == True:
            s += 1
            a.append(4)
        if self.checkBox_65.isChecked() == True:
            s += 1
            a.append(5)
        if self.checkBox_66.isChecked() == True:
            s += 1
            a.append(6)
        if self.checkBox_67.isChecked() == True:
            s += 1
            a.append(7)
        if self.checkBox_68.isChecked() == True:
            s += 1
            a.append(8)
        if self.checkBox_69.isChecked() == True:
            s += 1
            a.append(9)
        if self.checkBox_70.isChecked() == True:
            s += 1
            a.append(10)
        if self.checkBox_71.isChecked() == True:
            s += 1
            a.append(11)
        if self.checkBox_72.isChecked() == True:
            s += 1
            a.append(12)
        if self.checkBox_73.isChecked() == True:
            s += 1
            a.append(13)
        if self.checkBox_74.isChecked() == True:
            s += 1
            a.append(14)
        if self.checkBox_75.isChecked() == True:
            s += 1
            a.append(15)
        if self.checkBox_76.isChecked() == True:
            s += 1
            a.append(16)
        if self.checkBox_77.isChecked() == True:
            s += 1
            a.append(17)
        if self.checkBox_78.isChecked() == True:
            s += 1
            a.append(18)
        if self.checkBox_79.isChecked() == True:
            s += 1
            a.append(19)
        if self.checkBox_80.isChecked() == True:
            s += 1
            a.append(20)
        if s == 0:
            a = [0]
        return s,a

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
