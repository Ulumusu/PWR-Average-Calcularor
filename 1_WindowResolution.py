#!/usr/bin/python3


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt



class sredniapwr(QWidget):


        def __init__(self, parent=None):
                super().__init__(parent)

                
                self.window()
                  

        def window(self):

                
                
                #label
                et1=QLabel("Ocena:", self)
                et2=QLabel("Waga:", self)
                et3=QLabel("ŚREDNIA:",self)

                #set widget in tabela
                setT=QGridLayout()
                setT.addWidget(et1, 1, 0)
                setT.addWidget(et2, 1, 2)
                setT.addWidget(et3, 0, 1)

               #edition
                self.mark1write=QLineEdit() #one line text edit
                self.wage2write=QLineEdit()  
                self.avg3result=QLineEdit()

                self.avg3result.readonly= True   #only read
                self.avg3result.setToolTip('Wpisz ocene i podaj wage')

                setT.addWidget(self.mark1write, 2, 0)
                setT.addWidget(self.wage2write, 2, 2)
                setT.addWidget(self.avg3result, 1, 1)

                #buttons
                addbutton=QPushButton("&Dodaj do średniej", self)
                resetbutton=QPushButton("&Reset", self)
                exportbutton=QPushButton("&Zapisz wynik w txt", self)
                endbutton=QPushButton("&Koniec", self)
                endbutton.resize(endbutton.sizeHint())

                seth=QHBoxLayout()
                seth.addWidget(resetbutton)
                seth.addWidget(endbutton)
                seth.addWidget(exportbutton)


                setT.addLayout(seth, 5,0,1,3)
                setT.addWidget(addbutton, 4,0,1,3)
                
                
                #write settings in window
                self.setLayout(setT)

                #endfunction
                endbutton.clicked.connect(self.endApp)
                addbutton.clicked.connect(self.main)
                resetbutton.clicked.connect(self.main)
                exportbutton.clicked.connect(self.main)
                

                self.setGeometry(20, 20, 600, 150) #window size
                self.setWindowTitle('Średnia PWR')
                self.show()
                

        def endApp(self):
                self.close()

        def closeEvent(self, event):

                answer= QMessageBox.question(
                        self, 'Pytanie',
                        'Chcesz skończyć?',
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                
                if answer==QMessageBox.No:
                        event.ignore()
                else:
                        event.accept()
    
        def keyPressEvent(self, e):
                if e.key()==Qt.Key_Escape:
                        self.close()

        
        
        
        def main(self):
                player=self.sender()
                avg=0
                
                try:
                        #your numbers (mark and wage)
                        mark=float(self.mark1write.text())
                        wage=float(self.wage2write.text())
       
                        if player.text()=="&Dodaj do średniej":
                                wagehome.append(wage)
                                makeavg=mark*wage
                                markshome.append(makeavg)
                                avg=sum(markshome)/sum(wagehome)              
                                          
                        if player.text()=="&Reset":
                                QMessageBox.warning(self, "Reset", "Resetowanie wyniku", QMessageBox.Ok)
                                wagehome.clear()
                                markshome.clear()
                                avg==0

                        #show result
                        self.avg3result.setText(str(avg))
                                
    
                except:
                        #save to answer to txt
                        if player.text()=="&Zapisz wynik w txt":
                                QMessageBox.warning(self, "Informacja", "Wynik zostal zapisany tam gdzie plik. Dokument nazywa sie Wynik", QMessageBox.Ok) 
                                                        
                        #QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
                
                        
if __name__=='__main__':
        import sys

        #arrays
        wagehome=[]
        markshome=[]
        
        
        
        aplication=QApplication(sys.argv)   #object represent app
        window=sredniapwr()                 #object represent window
        sys.exit(aplication.exec_())        #main loop, sys.exit finish program





















        
