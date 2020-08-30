# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import parque_eolico_v2
import resultados_parque_eolico
import potencia_generada

class ResponseApp(QtWidgets.QMainWindow, resultados_parque_eolico.Ui_ResponseWindow):
    def __init__(self, parent=None):
        super(ResponseApp, self).__init__(parent)
        self.setupUi(self)
def response(self):
        response = ResponseApp(self)
        response.setMatriz(self.matriz_resultados)
        self.dialogs.append(response)
        response.show() 

class PotenciaApp(QtWidgets.QMainWindow, potencia_generada.Ui_PotenciaWindow):
    def __init__(self, parent=None):
        super(PotenciaApp, self).__init__(parent)
        self.setupUi(self)
def potencia(self):
        potencia = PotenciaApp(self)
        potencia.setPotencia(self.potencia_generada)
        potencia.setGraficoPotencia(self.grafico_resultados)
        self.dialogs.append(potencia)
        potencia.show() 

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        mainWindow.resize(800, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/img/aerogeneradores.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background: url(:/prefijoNuevo/aerogeneradores800.jpg);\n""")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(180, 10, 471, 31))
        self.titulo.setObjectName("titulo")
        self.subtitulo = QtWidgets.QLabel(self.centralwidget)
        self.subtitulo.setGeometry(QtCore.QRect(150, 50, 531, 21))
        self.subtitulo.setObjectName("subtitulo")
        self.titulo_configuracion = QtWidgets.QLabel(self.centralwidget)
        self.titulo_configuracion.setGeometry(QtCore.QRect(30, 80, 281, 17))
        self.titulo_configuracion.setObjectName("titulo_configuracion")
        self.titulo_aerogenerador = QtWidgets.QLabel(self.centralwidget)
        self.titulo_aerogenerador.setGeometry(QtCore.QRect(30, 390, 121, 17))
        self.titulo_aerogenerador.setObjectName("titulo_aerogenerador")
        self.titulo_ciudad = QtWidgets.QLabel(self.centralwidget)
        self.titulo_ciudad.setGeometry(QtCore.QRect(30, 116, 121, 17))
        self.titulo_ciudad.setObjectName("titulo_ciudad")
        self.radioButton_winwid = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_winwid.setGeometry(QtCore.QRect(30, 530, 200, 22))
        self.radioButton_winwid.setStyleSheet("color:black;\n")
        self.radioButton_winwid.setChecked(True)
        self.radioButton_winwid.setObjectName("radioButton_winwid")
        self.select_aerogenerador = QtWidgets.QButtonGroup(mainWindow)
        self.select_aerogenerador.setObjectName("select_aerogenerador")
        self.select_aerogenerador.addButton(self.radioButton_winwid)
        self.radioButton_vestas = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_vestas.setGeometry(QtCore.QRect(310, 530, 200, 22))
        self.radioButton_vestas.setStyleSheet("color:black;\n")
        self.radioButton_vestas.setObjectName("radioButton_vestas")
        self.select_aerogenerador.addButton(self.radioButton_vestas)
        self.radioButton_gamesa = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_gamesa.setGeometry(QtCore.QRect(580, 530, 200, 22))
        self.radioButton_gamesa.setStyleSheet("color:black;\n")
        self.radioButton_gamesa.setObjectName("radioButton_gamesa")
        self.select_aerogenerador.addButton(self.radioButton_gamesa)
        self.radioButton_zona1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_zona1.setGeometry(QtCore.QRect(490, 156, 80, 22))
        self.radioButton_zona1.setStyleSheet("color:black;\n")
        self.radioButton_zona1.setChecked(True)
        self.radioButton_zona1.setObjectName("radioButton_zona1")
        self.select_zona = QtWidgets.QButtonGroup(mainWindow)
        self.select_zona.setObjectName("select_zona")
        self.select_zona.addButton(self.radioButton_zona1)
        self.radioButton_zona2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_zona2.setGeometry(QtCore.QRect(490, 188, 80, 22))
        self.radioButton_zona2.setStyleSheet("color:black;\n")
        self.radioButton_zona2.setObjectName("radioButton_zona2")
        self.select_zona.addButton(self.radioButton_zona2)
        self.radioButton_zona3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_zona3.setGeometry(QtCore.QRect(490, 218, 80, 22))
        self.radioButton_zona3.setStyleSheet("color:black;\n")
        self.radioButton_zona3.setObjectName("radioButton_zona3")
        self.select_zona.addButton(self.radioButton_zona3)
        self.radioButton_zona4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_zona4.setGeometry(QtCore.QRect(490, 250, 80, 22))
        self.radioButton_zona4.setStyleSheet("color:black;\n")
        self.radioButton_zona4.setObjectName("radioButton_zona4")
        self.select_zona.addButton(self.radioButton_zona4)
        self.generarparque = QtWidgets.QPushButton(self.centralwidget)
        self.generarparque.setGeometry(QtCore.QRect(218, 590, 361, 27))
        self.generarparque.setStyleSheet("color:black;\n""background-color:green;")
        self.generarparque.setObjectName("generarparque")
        self.generarparque.clicked.connect(self.generar_parque)
        self.image_gamesa = QtWidgets.QWidget(self.centralwidget)
        self.image_gamesa.setGeometry(QtCore.QRect(30, 420, 200, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_gamesa.sizePolicy().hasHeightForWidth())
        self.image_gamesa.setSizePolicy(sizePolicy)
        self.image_gamesa.setAutoFillBackground(False)
        self.image_gamesa.setStyleSheet("background: url(:/prefijoNuevo/gamesa_min.jpg);\n"
"background-position: center; \n"
"background-repeat: no-repeat; ")
        self.image_gamesa.setObjectName("image_gamesa")
        self.image_vestas = QtWidgets.QWidget(self.centralwidget)
        self.image_vestas.setGeometry(QtCore.QRect(310, 420, 200, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_vestas.sizePolicy().hasHeightForWidth())
        self.image_vestas.setSizePolicy(sizePolicy)
        self.image_vestas.setAutoFillBackground(False)
        self.image_vestas.setStyleSheet("background: url(:/prefijoNuevo/vestas_min.jpg);\n"
"background-position: center; \n"
"background-repeat: no-repeat; ")
        self.image_vestas.setObjectName("image_vestas")
        self.image_winwid = QtWidgets.QWidget(self.centralwidget)
        self.image_winwid.setGeometry(QtCore.QRect(580, 420, 200, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_winwid.sizePolicy().hasHeightForWidth())
        self.image_winwid.setSizePolicy(sizePolicy)
        self.image_winwid.setAutoFillBackground(False)
        self.image_winwid.setStyleSheet("background: url(:/prefijoNuevo/winwind_min.jpg);\n"
"background-position: center; \n"
"background-repeat: no-repeat; ")
        self.image_winwid.setObjectName("image_winwid")
        self.radioButton_zona5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_zona5.setGeometry(QtCore.QRect(490, 282, 80, 22))
        self.radioButton_zona5.setStyleSheet("color:black;\n")
        self.radioButton_zona5.setObjectName("radioButton_zona5")
        self.select_zona.addButton(self.radioButton_zona5)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 110, 211, 251))
        self.widget.setStyleSheet("background: url(:/prefijoNuevo/vientosSantaFe.png);\n"
"background-position: center; \n"
"background-repeat: no-repeat; ")
        self.widget.setObjectName("widget")
        self.referencias = QtWidgets.QWidget(self.centralwidget)
        self.referencias.setGeometry(QtCore.QRect(410, 138, 81, 181))
        self.referencias.setStyleSheet("background: url(:/prefijoNuevo/referencias.png);\n"
"background-position: center; \n"
"background-repeat: no-repeat; ")
        self.referencias.setObjectName("referencias")
        self.titulo_viento = QtWidgets.QLabel(self.centralwidget)
        self.titulo_viento.setGeometry(QtCore.QRect(420, 130, 100, 17))
        self.titulo_viento.setObjectName("titulo_viento")
        mainWindow.setCentralWidget(self.centralwidget)
        self.matriz_resultados = None
        self.potencia_generada = None
        self.grafico_resultados = None
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    @QtCore.pyqtSlot()
    def generar_parque(self):
        lista_velocidades = [6.5,6,5.5,5,4.5]
        zona_elegida = lista_velocidades[[self.select_zona.buttons()[x].isChecked() for x in range(len(self.select_zona.buttons()))].index(True)]
        lista_aerogeneradores = ["gamesa","vestas","winwind"]
        aerogenerador_elegido = lista_aerogeneradores[[self.select_aerogenerador.buttons()[x].isChecked() for x in range(len(self.select_aerogenerador.buttons()))].index(True)]
        print("velocidad viento zona: ",zona_elegida)
        print("aerogenerador: ",aerogenerador_elegido)
        self.matriz_resultados,self.potencia_generada,self.grafico_resultados=parque_eolico_v2.programa_principal(zona_elegida,aerogenerador_elegido)
        potencia(self)
        response(self)
        
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Parque Eólico"))
        self.titulo.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:20pt;color:back\">Diseño de Parques Eólicos en Santa Fe</span></p></body></html>"))
        self.subtitulo.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;color:black\">Optimización de la energía generada utilizando algoritmos genéticos</span></p></body></html>"))
        self.titulo_configuracion.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;color:black\">Configurar diseño del Parque Eólico</span></p></body></html>"))
        self.titulo_aerogenerador.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;color:black\">Aerogenerador</span></p></body></html>"))
        self.titulo_ciudad.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;color:black\">Zona</span></p></body></html>"))
        self.radioButton_winwid.setText(_translate("mainWindow", "Gamesa G47"))
        self.radioButton_vestas.setText(_translate("mainWindow", "Vestas V90/3000"))
        self.radioButton_gamesa.setText(_translate("mainWindow", "Winwid WWD-3-10"))
        self.radioButton_zona1.setText(_translate("mainWindow", "Zona 1"))
        self.radioButton_zona2.setText(_translate("mainWindow", "Zona 2"))
        self.radioButton_zona3.setText(_translate("mainWindow", "Zona 3"))
        self.radioButton_zona4.setText(_translate("mainWindow", "Zona 4"))
        self.generarparque.setText(_translate("mainWindow", "Generar Diseño Optimizado"))
        self.radioButton_zona5.setText(_translate("mainWindow", "Zona 5"))
        self.titulo_viento.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;color:black\">Viento m/s</span></p></body></html>"))
        
import img_rc