import os
from pyreportjasper import PyReportJasper
from Control.SQLite_Database import DB  # Importamos la clase DB

    
def processing():
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Informes')
    entrada = os.path.join(REPORTS_DIR, 'Informe_Albaranes.jrxml')
    salida = os.path.join(REPORTS_DIR, 'Informe_Albaranes')
    pyreportjasper = PyReportJasper()
    
    # Crear instancia de la clase DB
    db = DB()
    con = db.obtener_conexion_sqlite()

    # Compilar el archivo .jrxml
    pyreportjasper.config(
        input_file=entrada,
        output_file=salida,
        output_formats=["pdf"],
        db_connection=con
    )

    pyreportjasper.compile(write_jasper=True)
    print("Compilación exitosa")
    # Procesar el informe
    pyreportjasper.process_report()
    print("Informe generado con éxito")

processing()



