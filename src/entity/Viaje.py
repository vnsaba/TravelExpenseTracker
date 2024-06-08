from datetime import datetime
import requests
from entity.Gasto import Gasto
from enums.TipoMoneda import TipoMoneda
class Viaje():
    def __init__(self, numero_viaje: str, destino: str, divisa: TipoMoneda, fecha_inicio: datetime,
                fecha_fin: datetime, presupuesto_diario: float, activo: bool):
        self.__numero_viaje = numero_viaje
        self.__destino = destino
        self.__divisa = divisa
        self.__fecha_inicio = fecha_inicio
        self.__fecha_final = fecha_fin
        self.__presupuesto_diario = presupuesto_diario
        self.__activo = activo
        self.__gastos = []
        self.__diferencia_presupuesto = presupuesto_diario
    
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
    
    def get_presupuesto(self):
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
    
    def get_gastos(self):
        return self.__gastos
    
    def adicionar_gasto(self, gasto: Gasto):
        self.__gastos.append(gasto)
        self.actualizar_diferencia_presupuesto()

    def actualizar_diferencia_presupuesto(self):
        total_gastado = sum(gasto.valor for gasto in self.__gastos)
        self.diferencia_presupuesto = self.__presupuesto_diario - total_gastado
        return self.__diferencia_presupuesto

    def mostrar_diferencia_presupuesto(self):
        return self.__diferencia_presupuesto

    def get_fecha_inicio(self):
        return datetime.strptime(self.__fecha_inicio, '%Y-%m-%d')

    def get_fecha_fin(self):
        return datetime.strptime(self.__fecha_final, '%Y-%m-%d')
    
    def presupuesto_convertido(self):
        presupuesto = 0
        if ((self.__divisa).upper() == "USD"):
            response = requests.get("https://v6.exchangerate-api.com/v6/26901b9538bf8ff8aeef69b6/pair/USD/COP")
            data = response.json()
            presupuesto = self.__presupuesto_diario * data['conversion_rate']
            self.set_presupuesto(presupuesto)
        elif ((self.__divisa).upper() == "EUR"):
            response = requests.get("https://v6.exchangerate-api.com/v6/26901b9538bf8ff8aeef69b6/pair/EUR/COP")
            data = response.json()
            presupuesto = self.__presupuesto_diario * data['conversion_rate']
            self.set_presupuesto(presupuesto)
        else:
            self.set_presupuesto(self.__presupuesto_diario)
            
    
    
    # def to_dict(self):
    #     return {
    #         "destino": self._destino,
    #         "fecha_inicio": self._fecha_inicio.strftime('%Y-%m-%d'),
    #         "fecha_final": self._fecha_final.strftime('%Y-%m-%d'),
    #         "presupuesto_diario": self._presupuesto_diario,
    #         "gastos": [g.to_dict() for g in self._gastos]
    #     }