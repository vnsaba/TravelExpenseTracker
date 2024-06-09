from datetime import datetime
import uuid
from ..entity.Gasto import Gasto
from ..enums.TipoMoneda import TipoMoneda

class Viaje():

    def __init__(self, destino: str, divisa: TipoMoneda, fecha_inicio: datetime,
                fecha_fin: datetime, presupuesto_diario: float):
        self.__numero_viaje = str(uuid.uuid4())  
        self.__destino = destino
        self.__divisa = divisa
        self.__fecha_inicio = fecha_inicio
        self.__fecha_final = fecha_fin
        self.__presupuesto_diario = presupuesto_diario
        self.__activo = True
        self.__gastos = []
    
    def get_activo(self):
        return self.__activo

    def set_activo(self, activo):
        self.__activo = activo
    
    def get_numero(self):
        return self.__numero_viaje
    
    def get_destino(self):
        return self.__destino
    
    def get_divisa(self):
        return self.__divisa
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_fecha_final(self):
        return self.__fecha_final
    
    def get_presupuesto_diario(self):
        return self.__presupuesto_diario
    
    def get_gastos(self):
        return self.__gastos
    
    def set_numero(self, numero):
        self.__numero_viaje = numero
    
    def set_destino(self, destino):
        self.__destino = destino
    
    def set_divisa(self, divisa):
        self.__divisa = divisa
        
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
        
    def set_fecha_final(self, fecha_final):
        self.__fecha_final = fecha_final
    
    def set_presupuesto(self, presupuesto):
        self.__presupuesto_diario = presupuesto

    def adicionar_gasto(self, gasto: Gasto):
        self.__gastos.append(gasto)
       # self.actualizar_diferencia_presupuesto()
    
    def imprimir_gastos(self):
        for gasto in self.__gastos:
            fecha = gasto.get_fecha().strftime('%Y-%m-%d')
            valor = gasto.get_valor()
            metodo_pago = gasto.get_metodo_pago().name  
            tipo_gasto = gasto.get_tipo_gasto().name    
            print(f"Fecha: {fecha}, Valor: {valor}, Método de Pago: {metodo_pago}, Tipo de Gasto: {tipo_gasto}")
