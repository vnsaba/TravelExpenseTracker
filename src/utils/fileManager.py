import json
from datetime import datetime
from entity.Viaje import Viaje
from entity.Gasto import Gasto

class FileManager():
    def __init__(self, filepath='../archivos/viajes.json'):
            self.filepath = filepath

    def cargar_viajes(self):
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return [
                    Viaje(
                        v['destino'],
                        datetime.strptime(v['fecha_inicio'], '%Y-%m-%d'),
                        datetime.strptime(v['fecha_final'], '%Y-%m-%d'),
                        v['presupuesto_diario'],
                        [Gasto(**g) for g in v.get('gastos', [])]  # Asumiendo que Gasto puede ser inicializado de esta manera
                    ) for v in data
                ]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
            return []

    def guardar_viajes(self, viajes):
        with open(self.filepath, 'w') as file:
            json.dump([viaje.to_dict() for viaje in viajes], file, default=str, indent=4)




