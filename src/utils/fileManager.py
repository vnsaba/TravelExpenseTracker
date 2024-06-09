import json
from pathlib import Path
from ..utils.ViajeSerializer import ViajeSerializer

class FileManager:

    def __init__(self, file_path='viajes.json'):
        self.file_path = Path(file_path)

    def guardar_viajes(self, viaje):
        """
        Guarda el viaje en un archivo JSON, agregando al archivo existente sin sobrescribirlo completamente.

        params:
            viaje (Viaje): Objeto de viaje a guardar

        Returns:
            bool: True si la operación fue exitosa, False en caso de error.
        """
        try:
            # Cargar viajes existentes si el archivo existe
            existing_data = []
            if self.existe_archivo():
                with self.file_path.open('r', encoding='utf-8') as file:
                    existing_data = json.load(file)
            
            new_data = ViajeSerializer.to_dict(viaje)
            existing_data.append(new_data)
            
            with self.file_path.open('w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al escribir los viajes en el archivo: {e}")
            return False
        
    def existe_archivo(self):
        """
        Verifica si el archivo JSON existe.

        Returns:
            bool: True si el archivo existe, False en caso contrario.
        """
        return self.file_path.exists()

    def cargar_viajes(self):
        if self.existe_archivo():
            with self.file_path.open('r', encoding='utf-8') as file:
                data = json.load(file)
                return [ViajeSerializer.from_dict(viaje_data) for viaje_data in data]
