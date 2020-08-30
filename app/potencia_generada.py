# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PotenciaWindow(object):
    def setPotencia(self,potencia):
        _translate = QtCore.QCoreApplication.translate
        self.potencia=potencia
        self.potenciaMax_titulo.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;color:black\">Potencia Máxima Generada: {}</span></p></body></html>".format(potencia)))
    def setGraficoPotencia(self,url):
        self.grafico_potencia.setStyleSheet("background: url(:/prefijoNuevo/{});\n""background-position: center; \n""background-repeat: no-repeat;".format(url))
    def setupUi(self, PotenciaWindow):
        PotenciaWindow.setObjectName("PotenciaWindow")
        PotenciaWindow.resize(800, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/prefijoNuevo/aerogeneradores.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PotenciaWindow.setWindowIcon(icon)
        PotenciaWindow.setStyleSheet("background: url(:/prefijoNuevo/aerogeneradores800.jpg);\n"
"")
        self.potenciaCentralwidget = QtWidgets.QWidget(PotenciaWindow)
        self.potenciaCentralwidget.setStyleSheet("background-color:white;")
        self.potenciaCentralwidget.setObjectName("potenciaCentralwidget")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.potencia_titulo = QtWidgets.QLabel(self.potenciaCentralwidget)
        self.potencia_titulo.setGeometry(QtCore.QRect(280, 10, 300, 40))
        self.potencia_titulo.setStyleSheet("color:black;")
        self.potencia_titulo.setObjectName("potencia_titulo")
        self.potenciaMax_titulo = QtWidgets.QLabel(self.potenciaCentralwidget)
        self.potenciaMax_titulo.setGeometry(QtCore.QRect(80, 60, 300, 40))
        self.potenciaMax_titulo.setStyleSheet("color:black;")
        self.potenciaMax_titulo.setObjectName("potenciaMax_titulo")        
        self.potencia = None
        self.grafico_potencia = QtWidgets.QWidget(self.potenciaCentralwidget)
        self.grafico_potencia.setGeometry(QtCore.QRect(80, 100, 640, 480))
        self.grafico_potencia.setObjectName("grafico_potencia")
        
        PotenciaWindow.setCentralWidget(self.potenciaCentralwidget)

        self.retranslateUi(PotenciaWindow)
        QtCore.QMetaObject.connectSlotsByName(PotenciaWindow)

    def retranslateUi(self, PotenciaWindow):
        _translate = QtCore.QCoreApplication.translate
        PotenciaWindow.setWindowTitle(_translate("PotenciaWindow", "Potencia Generada Parque Eólico"))
        self.potencia_titulo.setText(_translate("PotenciaWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Gráfico de potencias</span></p></body></html>"))
import img_rc
