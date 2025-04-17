import sys
import os

from PySide6.QtWidgets import QFileDialog, QInputDialog, QWidget, QApplication, QMessageBox, QLineEdit

from Control.Report_gen import ReportGenerator
from Vista.ui_main import Ui_MainWindow

class Reportes(QWidget, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

        self.report_generator = ReportGenerator()
    

        # Botones
        self.btnSelectJRXML.clicked.connect(self.seleccionar_ruta_jrxml)
        self.btnSelectPDF.clicked.connect(self.seleccionar_ruta_pdf)
        self.btnGenerar.clicked.connect(self.generar_informe)



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

    def cargar_clientes(self):
        """Carga los clientes desde la base de datos para usarlos como parámetros."""
        try:
            conexion = self.report_generator.db.obtener_conexion_sqlite()
            query = "SELECT ID_Cliente, Nombre FROM clientes"
            clientes = self.report_generator.db.ejecutar_consulta(query)
            return [f"{row[0]} - {row[1]}" for row in clientes]
        except Exception as e:
            self.textEditOutput.append(f"Error al cargar clientes: {str(e)}")
            return []

    def cargar_pedidos(self):
        """Carga los pedidos desde la base de datos para usarlos como parámetros."""
        try:
            conexion = self.report_generator.db.obtener_conexion_sqlite()
            query = "SELECT ID_Pedido, Fecha_Pedido FROM pedidos"
            pedidos = self.report_generator.db.ejecutar_consulta(query)
            return [f"{row[0]} - {row[1]}" for row in pedidos]
        except Exception as e:
            self.textEditOutput.append(f"Error al cargar pedidos: {str(e)}")
            return []
        
    def generar_informe(self):
        nombre_archivo = self.comboBoxJRXML.currentText()

        if not nombre_archivo or not self.ruta_jrxml or not self.ruta_pdf:
            QMessageBox.warning(
                self,
                "Faltan datos",
                "Por favor, completa todas las rutas y selecciona un informe.",
            )
            return

        ruta_jrxml = os.path.join(self.ruta_jrxml, nombre_archivo)
        ruta_salida = os.path.join(self.ruta_pdf, nombre_archivo.replace(".jrxml", ""))

        # Diccionario de parámetros específicos para informes
        diccionario_parametros = {
            "Informe_Albaran_filtrar_cliente": ("filtrar_cliente", self.pedir_parametros, self.cargar_clientes()),
            "Informe_Albaran_filtrar_pedido": ("filtrar_pedido", self.pedir_parametros, self.cargar_pedidos()),
        }

        # Obtener el nombre del informe sin extensión
        informe_clave = nombre_archivo.replace(".jrxml", "")

        # Obtener parámetros si el informe los requiere
        parametros = {}
        if informe_clave in diccionario_parametros:
            param_nombre, param_funcion, param_opciones = diccionario_parametros[informe_clave]
            valor_parametro = param_funcion(param_opciones)
            if valor_parametro:
                parametros[param_nombre] = int(valor_parametro.split(" - ")[0])  # Convertir a entero

        try:
            self.report_generator.generar_informe(ruta_jrxml, ruta_salida, parametros)
            ruta_salida_pdf = f"{ruta_salida}.pdf"
            if os.path.exists(ruta_salida_pdf):
                self.textEditOutput.append(
                    f"Informe generado exitosamente: {ruta_salida_pdf}"
                )
            else:
                self.textEditOutput.append("Error: El archivo no se generó.")

        except Exception as e:
            self.textEditOutput.append(f"Error al generar el informe: {str(e)}")
            QMessageBox.critical(
                self, "Error", f"No se pudo generar el informe: {str(e)}"
            )

    def pedir_parametros(self, opciones):
        """Solicita al usuario un parámetro de una lista de opciones."""
        pTitulo = "Parámetros"
        pTexto = "Selecciona un valor para el parámetro:"
        sel, conf = QInputDialog.getItem(self, pTitulo, pTexto, opciones, 0, False)
        if conf:
            print(f"Seleccionado: {sel}")
            return sel
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Reportes()
    mi_app.show()
    sys.exit(app.exec())
