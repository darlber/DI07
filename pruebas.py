import os
from pyreportjasper import PyReportJasper
from Control.SQLite_Database import DB  # Importamos la clase DB

"""
script para probar la generación de informes con pyreportjasper antes de implementarlo en la app
"""
    
def processing():
    REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Informes')
    entrada = os.path.join(REPORTS_DIR, 'Albaranes_sub.jrxml')
    salida = os.path.join(REPORTS_DIR, 'Albaranes_sub')
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
        db_connection=con
    )

    """process utiliza format_list"""
    
    
    pyreportjasper.compile(write_jasper=True) # Compila el archivo .jrxml y lo convierte a .jasper, recomendable si da error
    print("Compilación exitosa")
    # Procesar el informe
    pyreportjasper.process_report()
    print("Informe generado con éxito")

processing()



