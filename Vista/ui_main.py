# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingCundk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import Vista.logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 499)
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setSpacing(50)
        self.headerLayout.setObjectName(u"headerLayout")
        self.labelLogo = QLabel(MainWindow)
        self.labelLogo.setObjectName(u"labelLogo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
        self.labelLogo.setSizePolicy(sizePolicy)
        self.labelLogo.setMinimumSize(QSize(170, 100))
        self.labelLogo.setMaximumSize(QSize(170, 100))
        self.labelLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.labelLogo.setPixmap(QPixmap(u":/logo/logo.png"))
        self.labelLogo.setScaledContents(True)

        self.headerLayout.addWidget(self.labelLogo)

        self.labelCompanyName = QLabel(MainWindow)
        self.labelCompanyName.setObjectName(u"labelCompanyName")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labelCompanyName.setFont(font)
        self.labelCompanyName.setScaledContents(False)
        self.labelCompanyName.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.headerLayout.addWidget(self.labelCompanyName)


        self.verticalLayout.addLayout(self.headerLayout)

        self.layoutJRXML = QHBoxLayout()
        self.layoutJRXML.setObjectName(u"layoutJRXML")
        self.labelJRXML = QLabel(MainWindow)
        self.labelJRXML.setObjectName(u"labelJRXML")
        font1 = QFont()
        font1.setPointSize(12)
        self.labelJRXML.setFont(font1)

        self.layoutJRXML.addWidget(self.labelJRXML)

        self.lineEditJRXML = QLineEdit(MainWindow)
        self.lineEditJRXML.setObjectName(u"lineEditJRXML")
        self.lineEditJRXML.setFont(font1)

        self.layoutJRXML.addWidget(self.lineEditJRXML)

        self.btnSelectJRXML = QPushButton(MainWindow)
        self.btnSelectJRXML.setObjectName(u"btnSelectJRXML")
        self.btnSelectJRXML.setFont(font1)

        self.layoutJRXML.addWidget(self.btnSelectJRXML)


        self.verticalLayout.addLayout(self.layoutJRXML)

        self.layoutPDF = QHBoxLayout()
        self.layoutPDF.setObjectName(u"layoutPDF")
        self.labelPDF = QLabel(MainWindow)
        self.labelPDF.setObjectName(u"labelPDF")
        self.labelPDF.setFont(font1)

        self.layoutPDF.addWidget(self.labelPDF)

        self.lineEditPDF = QLineEdit(MainWindow)
        self.lineEditPDF.setObjectName(u"lineEditPDF")
        self.lineEditPDF.setFont(font1)

        self.layoutPDF.addWidget(self.lineEditPDF)

        self.btnSelectPDF = QPushButton(MainWindow)
        self.btnSelectPDF.setObjectName(u"btnSelectPDF")
        self.btnSelectPDF.setFont(font1)

        self.layoutPDF.addWidget(self.btnSelectPDF)


        self.verticalLayout.addLayout(self.layoutPDF)

        self.layoutComboJRXML = QHBoxLayout()
        self.layoutComboJRXML.setObjectName(u"layoutComboJRXML")
        self.labelSelectReport = QLabel(MainWindow)
        self.labelSelectReport.setObjectName(u"labelSelectReport")
        self.labelSelectReport.setFont(font1)

        self.layoutComboJRXML.addWidget(self.labelSelectReport)

        self.comboBoxJRXML = QComboBox(MainWindow)
        self.comboBoxJRXML.setObjectName(u"comboBoxJRXML")
        self.comboBoxJRXML.setFont(font1)

        self.layoutComboJRXML.addWidget(self.comboBoxJRXML)


        self.verticalLayout.addLayout(self.layoutComboJRXML)

        self.layoutParam = QHBoxLayout()
        self.layoutParam.setObjectName(u"layoutParam")


        self.verticalLayout.addLayout(self.layoutParam)

        self.btnGenerar = QPushButton(MainWindow)
        self.btnGenerar.setObjectName(u"btnGenerar")
        self.btnGenerar.setFont(font1)

        self.verticalLayout.addWidget(self.btnGenerar)

        self.textEditOutput = QTextEdit(MainWindow)
        self.textEditOutput.setObjectName(u"textEditOutput")
        self.textEditOutput.setMinimumSize(QSize(392, 192))
        font2 = QFont()
        font2.setPointSize(11)
        self.textEditOutput.setFont(font2)
        self.textEditOutput.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEditOutput)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Generador de Informes - SumiMet\u00e1licos, S.L.", None))
        self.labelCompanyName.setText(QCoreApplication.translate("MainWindow", u"SumiMet\u00e1licos, S.L.", None))
        self.labelJRXML.setText(QCoreApplication.translate("MainWindow", u"Ruta JRXML:", None))
        self.btnSelectJRXML.setText(QCoreApplication.translate("MainWindow", u"Seleccionar carpeta", None))
        self.labelPDF.setText(QCoreApplication.translate("MainWindow", u"Ruta PDF:", None))
        self.btnSelectPDF.setText(QCoreApplication.translate("MainWindow", u"Seleccionar carpeta", None))
        self.labelSelectReport.setText(QCoreApplication.translate("MainWindow", u"Informe a generar:", None))
    
        self.btnGenerar.setText(QCoreApplication.translate("MainWindow", u"Generar informe PDF", None))
        self.textEditOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mensajes del sistema...", None))
    # retranslateUi

