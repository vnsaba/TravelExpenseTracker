from datetime import datetime

class Viaje:
    def __init__(self, numero_viaje, destino, fecha_inicio, fecha_fin, presupuesto_diario):
        self._numero_viaje = numero_viaje
        self._destino = destino
        self._fecha_inicio = fecha_inicio
        self._fecha_final = fecha_fin
        self._presupuesto_diario = presupuesto_diario
        self._gastos = []
        self.diferencia_presupuesto = presupuesto_diario

    def agregar_gasto(self, gasto):
        self._gastos.append(gasto)
        self.actualizar_diferencia_presupuesto()

    def actualizar_diferencia_presupuesto(self):
        total_gastado = sum(gasto.valor for gasto in self._gastos)
        self.diferencia_presupuesto = self._presupuesto_diario - total_gastado

    def mostrar_diferencia_presupuesto(self):
        return self.diferencia_presupuesto

    def getFechaInicio(self):
        return datetime.strptime(self._fecha_inicio, '%Y-%m-%d')

    def getFechaFin(self):
        return datetime.strptime(self._fecha_final, '%Y-%m-%d')

    
    def getPresupuestoDiario (self):
        return self._presupuesto_diario
    
    # def to_dict(self):
    #     return {
    #         "destino": self._destino,
    #         "fecha_inicio": self._fecha_inicio.strftime('%Y-%m-%d'),
    #         "fecha_final": self._fecha_final.strftime('%Y-%m-%d'),
    #         "presupuesto_diario": self._presupuesto_diario,
    #         "gastos": [g.to_dict() for g in self._gastos]
    #     }