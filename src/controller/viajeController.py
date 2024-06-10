import logging
from ..enums.TipoMoneda import TipoMoneda
from ..utils.fileManager import FileManager
from datetime import datetime
from ..entity.Viaje import Viaje
from ..entity.Gasto import Gasto
from .ControllerConversorMoneda import ControllerConversorMoneda

class ViajeController():
    """Controlador para gestionar los viajes."""
    
    def __init__(self):
        self.__viaje = None
        self.file_manager = FileManager()
        self.__viajes = self.file_manager.cargar_viajes()
            
    def registrar_viaje(self, destino, divisa, fecha_inicio, fecha_fin, presupuesto):
        """
        Registra un nuevo viaje con los detalles proporcionados.

        params:
            destino (str): Nombre del destino del viaje.
            divisa (TipoDivisa): Tipo de divisa en la que se manejará el presupuesto del viaje.
            fecha_inicio (datetime): Fecha de inicio del viaje.
            fecha_fin (datetime): Fecha de finalización del viaje.
            presupuesto (float): Presupuesto diario asignado para el viaje.

        Returns:
            bool: True si el viaje fue registrado exitosamente, False si no se pudo registrar.
        """
        self.validar_presupuesto(presupuesto)
        self.validar_divisa(divisa)
    
        presupuesto = ControllerConversorMoneda.obtener_conversor(divisa, presupuesto)
  
        if self.verificar_fecha_inicio(fecha_inicio) and self.verificar_fecha_final(fecha_fin, fecha_inicio) and self.verificar_destino(destino):
            self.__viaje = Viaje(destino, divisa, fecha_inicio, fecha_fin, presupuesto)
            self.__viajes.append(self.__viaje)
            self.guardar_viajes_en_archivo()
            return True
        return False
    
    def validar_divisa(self, divisa):
        if divisa not in TipoMoneda.__members__.values():
            raise AttributeError("La divisa no es válida.")
    
    def validar_presupuesto(self, presupuesto: float):
        """
        Valida que el presupuesto sea mayor que cero.

        param:
            presupuesto (float): Presupuesto a validar.

        Raises:
            ValueError: Si el presupuesto es menor a cero.
        """
        if presupuesto < 0:
            raise ValueError("El presupuesto debe ser mayor que cero.")
    
    def verificar_fecha_inicio(self, fecha_inicio: datetime):
        """
        Verifica si la fecha de inicio es válida.

        params:
            fecha_inicio (datetime): La fecha de inicio del viaje.

        Returns:
            bool: True si la fecha de inicio es válida, False en caso contrario.
        """
        ahora = datetime.now()
        if fecha_inicio < ahora:
            return False
        return True
    
    def verificar_fecha_final(self, fecha_fin: datetime, fecha_inicio: datetime):
        """
        Verifica si la fecha de finalización es válida en relación a la fecha de inicio.

        params:
            fecha_fin (datetime): La fecha de finalización del viaje.
            fecha_inicio (datetime): La fecha de inicio del viaje.

        Returns:
            bool: True si la fecha de finalización es válida, False en caso contrario.
        """
        if fecha_fin <= fecha_inicio:
            return False
        return True
    
    def verificar_destino(self, destino: str) -> bool:
        """
        Verifica si el destino ingresado es válido.

        params:
            destino (str): El destino del viaje a verificar.

        Returns:
            bool: True si el destino es válido, False en caso contrario.
        """
        if not destino.strip(): 
            print("El destino no puede estar vacío.")
            return False
        return True
    
    def buscar_viaje(self, numero: str):
        for viaje in self.__viajes:
            if viaje.get_numero() == numero:
                return viaje
        return None

    def verificar_fecha_viaje(self, fecha_inicio, fecha_fin):
        """
        Verifica si hay algún viaje con la misma fecha de inicio o la misma fecha final.

        Retorna:
        - False si hay algún viaje con la misma fecha de inicio o final. True de lo contrario.
        """
        for viaje in self.__viajes:  
            if viaje.get_fecha_inicio() == fecha_inicio or viaje.get_fecha_final() == fecha_fin:
                return False
        return True

    
    def esta_activo(self, numero: str):
        viaje = self.buscar_viaje(numero)
        if viaje == None:
            return False
        return viaje.get_activo()

    def verificar_fecha_gasto(self, fecha_gasto: datetime, viaje_actual):
        """
        Verifica si la fecha del gasto está dentro del rango de fechas del viaje actual.

        params:
            fecha_gasto (datetime): Fecha del gasto a verificar.
            viaje_actual: Número del viaje actual.

        Returns:
            bool: True si la fecha del gasto está dentro del rango de fechas del viaje actual, False en caso contrario.
        """
        for viaje in self.__viajes:
            if viaje.get_numero() == viaje_actual and viaje.get_activo():
                if viaje.get_fecha_inicio() <= fecha_gasto <= viaje.get_fecha_final():
                    return True
        return False

    def divisa(self):
        """
        Retorna la divisa del viaje actual.
        
        Returns:
            TipoMoneda: La divisa del viaje actual.
            None: Si no hay un viaje actual.
        """
        if self.__viaje is None:
            print("Error: No hay un viaje activo.")
            return None
        
        return self.__viaje.get_divisa()
              

    def adicionar_gasto(self, gasto: Gasto):
        """
        Añade un gasto al viaje actual si la fecha del gasto está dentro del rango de fechas del viaje.

        params:
            gasto: Objeto del tipo Gasto a añadir al viaje.

        Returns:
            bool: True si el gasto fue añadido correctamente al viaje, False si no se pudo añadir.
        """
        if self.verificar_fecha_gasto(gasto.get_fecha(), self.__viaje.get_numero()):
            self.__viaje.adicionar_gasto(gasto)
            return True
        return False
    
    def get_viaje(self):
        """
        Obtiene el viaje actual.

        Returns:
            Viaje: Objeto del tipo Viaje que representa el viaje actual.
        """
        return self.__viaje
        
    def lista_gastos(self):
        """
        Lista los gastos del viaje actual.

        Prints:
            Mensajes sobre los gastos del viaje actual o que no hay viajes registrados.
        """
        if not self.__viajes:
            print("No hay viajes registrados.")
            return
        print(f"---- {self.__viaje.get_destino()} - Presupuesto Diario: {self.__viaje.get_presupuesto_diario()} ----")
        self.get_viaje().imprimir_gastos()
        
    def guardar_viajes_en_archivo(self):
        """
        Guarda la lista de viajes actuales en un archivo JSON.

        Returns:
            bool: True si los viajes se guardaron exitosamente, False en caso contrario.
        """
        return self.file_manager.guardar_viajes(self.__viaje)
    
    def lista_viajes(self):
        """Lista todos los viajes registrados y sus respectivos gastos."""
        viajes = self.file_manager.cargar_viajes()
        if not viajes:
            print("No hay viajes registrados en el archivo.")
            return
        
        for viaje in viajes:
            print(f"Viaje a {viaje.get_destino()} - Número: {viaje.get_numero()}")
            print(f"  - Fechas: {viaje.get_fecha_inicio()} a {viaje.get_fecha_final()}")
            print(f"  - Presupuesto Diario: {viaje.get_presupuesto_diario()} {viaje.get_divisa().name}")
            print(f"  - Gastos:")
            for gasto in viaje.get_gastos():
                print(f"    - {gasto.get_tipo_gasto().name}: {gasto.get_valor()} {viaje.get_divisa().name} (Fecha: {gasto.get_fecha()})")
            print()










