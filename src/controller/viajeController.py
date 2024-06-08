from utils import FileManager
from datetime import datetime
from entity.Viaje import Viaje

class ViajeController():
    
    FECHA_ACTUAL = datetime.now()

    def __init__(self):
        self.__viaje = None
        self.__viajes = []
        self.__file_manager = FileManager()
    
    def registrar_viaje(self, numero, destino, divisa, fecha_inicio, fecha_fin, presupuesto, activo):
        self.__viaje = Viaje(numero, destino, divisa, fecha_inicio, fecha_fin, presupuesto, activo)
        self.__viajes.append(self.__viaje)
        self.__file_manager.guardar_viajes(self.__viajes)
    
    def verificar_fecha_inicio(self, fecha_inicio: datetime):
        if (fecha_inicio < self.FECHA_ACTUAL):
            return False
        self.__viaje.set_fecha_inicio(fecha_inicio)
        return True
    
    def verificar_presupuesto(self, monto: float) -> bool:
        if monto > 0:
            if self.__viaje.get_presupuesto() > 0 and self.__viaje.get_presupuesto() >= monto:
                self.__viaje.set_presupuesto(self.__viaje.get_presupuesto() - monto)
                return True
        return False
    
    def verificar_fecha_final(self, fecha_fin: datetime, fecha_inicio: datetime):
        if fecha_fin <= fecha_inicio :
            return False
        self.__viaje.set_fecha_final(fecha_fin)
        return True
    
    def verificar_destino(self, destino: str):
        if destino == "":
            return False
        self.__viaje.set_destino(destino)
        return True
    
    def buscar_viaje(self, numero: str):
        for viaje in self.__viajes:
            if viaje.get_numero() == numero:
                return viaje
        return None
    
    def esta_activo(self, numero: str):
        viaje = self.buscar_viaje(numero)
        if viaje == None:
            return False
        return viaje.get_activo()

    def verificar_fecha_gasto(self, fecha_gasto: datetime):
        for viaje in self.__viajes:
            if viaje.get_activo():
                if viaje.get_fecha_inicio() <= fecha_gasto <= viaje.get_fecha_final():
                    return True
        return False

    def adicionar_gasto(self, gasto):
        if self.verificar_fecha_gasto(gasto.get_fecha()):
            self.__viaje.adicionar_gasto(gasto)
            self.__viaje.set_presupuesto(self.__viaje.get_presupuesto() - gasto.get_valor())
            self.__file_manager.guardar_viajes(self.__viajes)
            return True
        return False
    
    
        
            
            
        

