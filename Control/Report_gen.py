import os
from PySide6.QtWidgets import QComboBox, QInputDialog, QMessageBox
import pyreportjasper
from Control.SQLite_Database import DB


class ReportGenerator:
    def __init__(self):
        self.db = DB()

    def generar_informe(self, ruta_jrxml, ruta_salida, parametros):
        """Genera un informe con los parámetros proporcionados"""
        try:

            # Si no se proporcionan parámetros, detectarlos automáticamente
            if parametros is None:
                nombre_informe = os.path.splitext(os.path.basename(ruta_jrxml))[0]
                # params_requeridos = self.db.obtener_parametros_informe(ruta_jrxml)

                # if params_requeridos:
                #   parametros = self.solicitar_parametros(nombre_informe, params_requeridos)
                #  if parametros is None:  # Usuario canceló
                #     return False, "Generación cancelada por el usuario"

            # Generar el informe
            conexion = self.db.obtener_conexion_sqlite()
            jasper = pyreportjasper.PyReportJasper()

            print(f"Parametros recibidos antes del jasper.process: {parametros} ")
            print("--" * 20)
            jasper.process(
                input_file=ruta_jrxml,
                output_file=ruta_salida,
                format_list=["pdf"],
                db_connection=conexion,
                parameters=parametros, 
                locale="es_ES",
            )

            # Verificar si el archivo de salida ya existe
            if not os.path.exists(f"{ruta_salida}.pdf"):
                raise FileNotFoundError(
                    f"No se generó el archivo de salida: {ruta_salida}.pdf"
                )

            return True, f"Informe generado correctamente en {ruta_salida}.pdf"

        except Exception as e:
            return False, f"Error al generar informe: {str(e)}"
