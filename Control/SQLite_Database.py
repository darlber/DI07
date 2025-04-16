import os
import pyreportjasper

class DB:
    _instance = None

    def __init__(self):
        self.jasper = pyreportjasper.PyReportJasper()
        
        
    # Singleton pattern to ensure only one instance of DB exists
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def obtener_conexion_sqlite(self):
            # Retrocede dos niveles desde el directorio actual (CONTROL -> DI07)
        project_root = os.path.dirname(os.path.dirname(__file__))
        jdbc_path = os.path.join(project_root, 'libs', 'jdbc', 'sqlite-jdbc-3.49.1.0.jar')
        return {
            'driver': 'sqlite',
            'jdbc_driver': 'org.sqlite.JDBC',
            'jdbc_dir': jdbc_path,
            'data_file': './Modelo/fabrica.db'
        }
        
    def obtener_parametros_informe(self, ruta_jrxml):
        """Obtiene los parámetros requeridos por un informe JRXML"""
        try:
            self.jasper.config(input_file=ruta_jrxml)
            return self.jasper.list_report_params()
        except Exception as e:
            raise Exception(f"Error al leer parámetros del informe: {str(e)}")
        
    def execute_query(self, connection_config, query):
        """Ejecuta una consulta SQL y retorna los resultados"""
        self.jasper.db_connection = connection_config
        return self.jasper.execute_sql(query)