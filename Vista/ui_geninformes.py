# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geninformesfhjOBq.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide6.QtCore import (QCoreApplication, QRect)
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QWidget, QMessageBox,QInputDialog)
from Control import crearinforme

class Ui_Form(object):
        
   
    
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.btnGenInforme = QPushButton(Form)
        self.btnGenInforme.setObjectName(u"btnGenInforme")
        self.btnGenInforme.setGeometry(QRect(270, 100, 111, 23))
        self.comboBoxFicheros = QComboBox(Form)
        self.comboBoxFicheros.setObjectName(u"comboBoxFicheros")
        self.comboBoxFicheros.setGeometry(QRect(20, 100, 231, 23))
        self.cdrTxtRutaSalida = QLineEdit(Form)
        self.cdrTxtRutaSalida.setObjectName(u"cdrTxtRuta")
        self.cdrTxtRutaSalida.setGeometry(QRect(40, 180, 281, 23))
        self.cdrTxtRutaEntrada = QLineEdit(Form)
        self.cdrTxtRutaEntrada.setObjectName(u"cdrTxtRuta_2")
        self.cdrTxtRutaEntrada.setGeometry(QRect(20, 40, 281, 23))
        """self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 40, 111, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 111, 20))
      """
        self.retranslateUi(Form)

        self.cdrTxtRutaEntrada.returnPressed.connect(self.cambiar_ruta)
        self.btnGenInforme.clicked.connect(self.generar_informe)
        try:
            self.comboBoxFicheros.addItems(os.listdir(self.cdrTxtRutaEntrada.text()))
        except FileNotFoundError:
            self.aviso("Aviso ruta de entrada","Indica la ruta de los ficheros jrxml")
            
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Generar Informes F\u00e1brica", None))
        self.btnGenInforme.setText(QCoreApplication.translate("Form", u"Generar Informe", None))
        #self.cdrTxtRutaSalida.setText(QCoreApplication.translate("Form", u"/home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/informes/pdf", None))
        self.cdrTxtRutaSalida.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros generados", None))
        self.cdrTxtRutaEntrada.setPlaceholderText(QCoreApplication.translate("Form", u"Ruta ficheros jrxml", None))
        self.cdrTxtRutaEntrada.setToolTip(QCoreApplication.translate("Form", u"Pulsar enter para actualizar la lista de ficherps", None))
        #self.cdrTxtRutaEntrada.setText(QCoreApplication.translate("Form", u"/home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/informes", None))
    # retranslateUi

    def aviso(self,titulo,texto):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Aviso")
        dialogo.setText(texto)
        dialogo.exec()
    
    def pedir_parametros(self,pLista):
        #dialogo = QInputDialog.getText(self, pTitulo, pTexto)
        pTitulo = "Parámetros"
        pTexto = "Parámetros"
        sel, conf = QInputDialog.getItem(self, pTitulo, pTexto, pLista)
        if conf:
            return sel
    

    def error(self,pLista):
       return ""

    def generar_informe(self):
        
        # tupla control error si el fichero no está en eñ diccionario sql_param
        mens_error=("",self.error,"")
        """ 
        /home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/informes
        asumo que si se han listado los ficheros, el directorio de entrada existe
            en cambio el de salida puede no existir, en ese caso aviso y genero en el directorio 
            de entrada
      """  
        """
        diccionario sel_param. Clave fichero a procesar.
        Dato tupla con el texto a mostrar
        al solicitar el parámetro (no lo estoy empleando. Mejora a futuro), método que solicita parámetro
        , en el caso que sea necesario, lista ara elegir 
        """
        sel_param={'Informe_4_1_1_1_parametro_texto': 
        ('Comentario', self.pedir_parametros,""),
    'Informe_4_1_1_filtrado_datos':('Ciudad', self.pedir_parametros,
                    ['Almendralejo','Cáceres','Madrid','Salamanca','Santander','Sevilla']),
    'Informe_4_1_1_ordenar_datos':('Orden', self.pedir_parametros,['Ciudad','Direccion','Nombre']),
    'Informe_4_7_1_Graficos': ('Titulo', self.pedir_parametros,""),
    'Informe_4_5_1_InformePrincipal': ('Titulo', self.pedir_parametros,"")}  

    #InformePrincipal necesita indicar correctamente la ruta relativa de logo.png y de 
    #Subinformes....jasper
    # Modificar en JaspeSoft, en lugar de fichero o ./fichero debe ser informes/fichero
        
        ficheroEntrada = self.cdrTxtRutaEntrada.text()+"/"+self.comboBoxFicheros.currentText()
        #obtener el fichero seleccionado sin la extensión, para generar con .pdf
        ficheroSalida =  self.cdrTxtRutaSalida.text()+"/"+self.comboBoxFicheros.currentText()[:-6]
        if not os.path.exists(self.cdrTxtRutaSalida.text()): 
            ficheroSalida = ficheroEntrada[:-6]
            self.aviso("Atención","El directorio de salida "+self.cdrTxtRutaSalida.text()+" no existe\nInformes en directorio de entrada")

        
        
        #obtener el fichero seleccionado sin la extensión, para utilizarlo como clave en diccionario
        fichero_sel=self.comboBoxFicheros.currentText()[:-6]

        #Obtener parámetros en formato diccionario: {Nombre_parametro : parametro}
        #Con métodos get de diccionario, si no existe la clave, evitamos error, ejecutando método
        #error en tupla mens_error
        #elemento 0, es la clave del diccionario parametros o Nombre_parametro
        #elemento 1, es el parámetro, que se obtiene al ejecutar la función self.pedir_parametro
        #(el parámetro de la función self.pedir_parametro es el elemento 2)
        parametros={sel_param.get(fichero_sel,mens_error)[0]:
                    sel_param.get(fichero_sel,mens_error)[1]
                    (sel_param.get(fichero_sel,mens_error)[2])}

        crearinforme.advanced_example_using_database(ficheroEntrada,ficheroSalida,parametros)

        # Habrá que modificar pyreportjasper.py  para controlar el error si el fichero no tiene
        #formato adecuado    
   
    def cambiar_ruta(self):  
        try:
            self.comboBoxFicheros.clear()
            items=os.listdir(self.cdrTxtRutaEntrada.text())
            #os.listdir(self.cdrTxtRutaEntrada.text()).sort()
            items.sort()
              
            self.comboBoxFicheros.addItems(items)
            
        except FileNotFoundError:
            self.aviso("Al cambiar ruta","No existe el directorio "+self.cdrTxtRutaEntrada.text())

import sys #Para que permita cerrar la ventana

class MiApp(QWidget,Ui_Form):
    # clase principal que crea nuestro interfaz
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       

   
if __name__ == "__main__":
    # Si no es utilizado como módulo, se jecutará
    #Simplemente abre la correspondiente ventana
    app = QApplication(sys.argv)
    mi_app = MiApp()
   
    mi_app.show()
    sys.exit(app.exec())