import os
from PySide6.QtWidgets import QComboBox, QInputDialog, QMessageBox
import pyreportjasper
from Control.SQLite_Database import DB

class ReportGenerator:
    def __init__(self, db):
        self.db = db
        self.param_config = {
            # Configuración especial para cada tipo de informe
            "Listado_clientes": {
                "filtrar_cliente": {
                    "tipo": "combo",
                    "titulo": "Filtrar por Cliente",
                    "consulta": "SELECT ID_Cliente, Nombre FROM clientes ORDER BY Nombre",
                    "formato": lambda row: f"{row[0]} - {row[1]}"
                }
            },
            "Listado_pedidos": {
                "filtrar_pedido": {
                    "tipo": "combo",
                    "titulo": "Filtrar por Pedido",
                    "consulta": "SELECT p.ID_Pedido, c.Nombre FROM pedidos p JOIN clientes c ON p.ID_Cliente = c.ID_Cliente ORDER BY p.ID_Pedido",
                    "formato": lambda row: f"{row[0]} - {row[1]}"
                }
            }
        }

    def generar_informe(self, ruta_jrxml, ruta_salida, parametros=None):
        """Genera un informe con los parámetros proporcionados"""
        try:
            
            # Si no se proporcionan parámetros, detectarlos automáticamente
            if parametros is None:
                nombre_informe = os.path.splitext(os.path.basename(ruta_jrxml))[0]
                #params_requeridos = self.db.obtener_parametros_informe(ruta_jrxml)
                
                #if params_requeridos:
                 #   parametros = self.solicitar_parametros(nombre_informe, params_requeridos)
                  #  if parametros is None:  # Usuario canceló
                   #     return False, "Generación cancelada por el usuario"
            
            # Generar el informe
            conexion = self.db.obtener_conexion_sqlite()
            jasper = pyreportjasper.PyReportJasper()

            jasper.process(
                input_file=ruta_jrxml,
                output_file=ruta_salida,
                format_list=["pdf"],
                parameters=parametros or {},  # Asegurar que no sea None
                db_connection=conexion
            )
            
            # Verificar si el archivo de salida ya existe
            if not os.path.exists(f"{ruta_salida}.pdf"):
                raise FileNotFoundError(f"No se generó el archivo de salida: {ruta_salida}.pdf")
            
            return True, f"Informe generado correctamente en {ruta_salida}.pdf"
            
        except Exception as e:
            return False, f"Error al generar informe: {str(e)}"
            
            
    def obtener_opciones_desde_bd(self, consulta, formato):
        """Obtiene opciones para combobox desde la base de datos"""
        try:
            conexion = self.db.obtener_conexion_sqlite()
            jasper = pyreportjasper.PyReportJasper()
            result = jasper.execute_query(conexion, consulta)
            return [formato(row) for row in result]
        except Exception as e:
            QMessageBox.warning(None, "Error", f"No se pudieron cargar las opciones: {str(e)}")
            return []

    def solicitar_parametros(self, nombre_informe, parametros_reales):
        """Solicita parámetros al usuario basado en la configuración"""
        parametros = {}
        
        # Obtener configuración especial para este informe
        config_especial = self.param_config.get(nombre_informe, {})
        
        for param in parametros_reales:
            if param in config_especial:
                # Parámetro con configuración especial
                config = config_especial[param]
                
                if config["tipo"] == "combo":
                    # Obtener opciones desde la base de datos
                    opciones = self.obtener_opciones_desde_bd(
                        config["consulta"], 
                        config["formato"]
                    )
                    
                    if not opciones:
                        return None  # Cancelar si no hay opciones
                    
                    # Mostrar diálogo para seleccionar
                    combo = QComboBox()
                    combo.addItems(opciones)
                    
                    dialog = QInputDialog()
                    dialog.setComboBox(combo)
                    dialog.setWindowTitle(config["titulo"])
                    dialog.setLabelText(f"Seleccione {param}:")
                    
                    if dialog.exec():
                        # Extraer el ID del valor seleccionado (primero antes del '-')
                        valor_seleccionado = combo.currentText()
                        valor = valor_seleccionado.split(" - ")[0]
                        parametros[param] = valor
                    else:
                        return None  # Usuario canceló
            else:
                # Parámetro genérico (texto libre)
                valor, ok = QInputDialog.getText(
                    None,
                    f"Parámetro requerido",
                    f"Ingrese valor para {param}:"
                )
                if ok:
                    parametros[param] = valor
                else:
                    return None  # Usuario canceló
        
        return parametros