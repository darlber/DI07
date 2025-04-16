import sys
import os

from PySide6.QtWidgets import QFileDialog, QWidget, QApplication, QMessageBox, QLineEdit
import pyreportjasper
from platform import python_version

from Control.Report_gen import ReportGenerator
from Control.SQLite_Database import DB
from Vista.ui_main import Ui_MainWindow


class Reportes(QWidget, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.DB = DB()
        self.report_generator = ReportGenerator(self.DB)
        self.probarConnectionDatabase()
   
        # Botones
        self.btnSelectJRXML.clicked.connect(self.seleccionar_ruta_jrxml)
        self.btnSelectPDF.clicked.connect(self.seleccionar_ruta_pdf)
        self.btnGenerar.clicked.connect(self.generar_informe)

        # Rutas y archivos
        self.ruta_jrxml = "C:/Users/darlb/Desktop/DI07/Informes"
        self.ruta_pdf = "C:/Users/darlb/Desktop/DI07/Informes/PDF"
        self.cargar_archivos_jrxml()


    def probarConnectionDatabase(self):
        try:
            path_db = self.DB.obtener_conexion_sqlite()["data_file"]
            if os.path.isfile(path_db):
                self.textEditOutput.append("Conexión a la base de datos establecida.")
            else:
                self.textEditOutput.append(
                    "No se encontró el archivo de base de datos."
                )
        except Exception as e:
            self.textEditOutput.append(
                f"Error al conectar a la base de datos: {str(e)}"
            )
            QMessageBox.critical(
                self, "Error", f"No se pudo conectar a la base de datos: {str(e)}"
            )

    def seleccionar_ruta_jrxml(self):
        ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta con JRXML")
        if ruta:
            self.ruta_jrxml = ruta
            self.lineEditJRXML.setText(ruta)
            self.cargar_archivos_jrxml()

    def seleccionar_ruta_pdf(self):
        ruta = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta para PDFs")
        if ruta:
            self.ruta_pdf = ruta
            self.lineEditPDF.setText(ruta)

    def cargar_archivos_jrxml(self):
        self.comboBoxJRXML.clear()
        if os.path.isdir(self.ruta_jrxml):
            archivos = [f for f in os.listdir(self.ruta_jrxml) if f.endswith(".jrxml")]
            self.comboBoxJRXML.addItems(archivos)
            self.textEditOutput.append(f"{len(archivos)} archivos JRXML encontrados.")
        else:
            self.textEditOutput.append("Ruta JRXML inválida.")

    def generar_informe(self):
        nombre_archivo = self.comboBoxJRXML.currentText()
        parametro = self.lineEditParam.text()

        if not nombre_archivo or not self.ruta_jrxml or not self.ruta_pdf:
            QMessageBox.warning(
                self,
                "Faltan datos",
                "Por favor, completa todas las rutas y selecciona un informe.",
            )
            return

        ruta_jrxml = os.path.join(self.ruta_jrxml, nombre_archivo)
        ruta_salida = os.path.join(self.ruta_pdf, nombre_archivo.replace(".jrxml", ""))
       
        parametros = {}

        try:
            self.report_generator.generar_informe(ruta_jrxml, ruta_salida, parametros)
            self.textEditOutput.append(
                f"Informe generado con éxito en: {ruta_salida}.pdf"
            )
        except Exception as e:
            self.textEditOutput.append(f"Error al generar el informe: {str(e)}")
            QMessageBox.critical(
                self, "Error", f"No se pudo generar el informe: {str(e)}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Reportes()
    mi_app.show()

    sys.exit(app.exec())
