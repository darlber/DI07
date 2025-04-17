import os
from pyreportjasper import PyReportJasper
from Control.SQLite_Database import DB  # Importamos la clase DB

"""
script para probar la generación de informes con pyreportjasper antes de implementarlo en la app
"""


def processing():
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Informes")
    entrada = os.path.join(REPORTS_DIR, "Informe_Ventas.jrxml")
    salida = os.path.join(REPORTS_DIR, "Informe_Ventas")
    pyreportjasper = PyReportJasper()

    # Crear instancia de la clase DB
    db = DB()
    con = db.obtener_conexion_sqlite()

    # Compilar el archivo .jrxml
    """config usa output_formats
    """
    pyreportjasper.config(
        input_file=entrada,
        output_file=salida,
        output_formats=["pdf"],
        db_connection=con,
    )

    """process utiliza format_list"""

    print(pyreportjasper.list_report_params())
    # Lista los parámetros del informe
    pyreportjasper.compile(write_jasper=True)
    print("Compilación exitosa")

    pyreportjasper.process_report()
    print("Informe generado con éxito")


""" Esto para probar los informes con parametros, no funciona con config

    pyreportjasper.process(
        input_file=entrada,
        output_file=salida,
        format_list=["pdf"],
        parameters={  # Asegurar que no sea None
            "filtrar_cliente": 1
        },
        db_connection=con,
        locale='es_ES'  # Cambia a tu configuración regional deseada
    )

"""
processing()
