﻿import os
import pyreportjasper
import sqlite3

class DB:
    _instance = None

    def __init__(self):
        self.jasper = pyreportjasper.PyReportJasper()
        self.conexion = None
        
        
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

    def conectar_sqlite(self):
        """Establece una conexión directa con la base de datos SQLite."""
        try:
            if self.conexion is None:
                self.conexion = sqlite3.connect('C:/Users/darlb/Desktop/DI07/Modelo/fabrica.db')
            return self.conexion
        except sqlite3.Error as e:
            print(f"Error al conectar con SQLite: {str(e)}")
            raise

    def ejecutar_consulta(self, query):
        """Ejecuta una consulta SQL y devuelve los resultados."""
        try:
            conexion = self.conectar_sqlite()
            cursor = conexion.cursor()
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Consulta ejecutada correctamente:", query)
            print("Resultados:", resultados)
            return resultados
        
        except sqlite3.Error as e:
            print(f"Error al ejecutar consulta: {str(e)}")
            raise