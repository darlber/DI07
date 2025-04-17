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
        try:
            # Retrocede dos niveles desde el directorio actual (CONTROL -> DI07)
            
            jdbc_path = os.path.join(os.path.dirname(pyreportjasper.__file__), 'libs', 'jdbc', 'sqlite-jdbc-3.49.1.0.jar')
            if not os.path.exists(jdbc_path):
                raise FileNotFoundError(f"El archivo JDBC no existe en la ruta especificada: {jdbc_path}")
            print("Archivo JDBC encontrado:", jdbc_path)
            conexion = {
                'driver': 'sqlite',
                'jdbc_driver': 'org.sqlite.JDBC',
                'jdbc_dir': 'libs/jdbc/sqlite-jdbc-3.49.1.0.jar',
                'data_file': 'C:/Users/darlb/Desktop/DI07/Modelo/fabrica.db',
            }
            print("Conexión SQLite configurada correctamente:", conexion)
            return conexion
        except Exception as e:
            print("Error al configurar la conexión SQLite:", str(e))
            raise
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