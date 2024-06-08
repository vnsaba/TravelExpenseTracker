from datetime import datetime
from enums.TipoMoneda import TipoMoneda
from enums.MetodoPago import MetodoPago
from enums.TipoGasto import TipoGasto
from entity.Gasto import Gasto
from controller.ConversorMoneda import ConversorMoneda
from controller.ViajeController import ViajeController

class GastoController():

    def __init__(self):
        self.__viaje_controller = ViajeController()
    
    def verificar_viaje(self, numero: str):
        viaje = self.__viaje_controller.buscar_viaje(numero)
        if viaje == None:
            print("El viaje no existe.")
            return False
        return True

    def registrar_gasto(self, fecha: datetime, monto: float, divisa: TipoMoneda, 
                       metodo_pago: MetodoPago, tipo_gasto: TipoGasto):
        if divisa == TipoMoneda.COP:
            gasto = Gasto(fecha, monto, divisa, metodo_pago, tipo_gasto)
        elif divisa == TipoMoneda.USD:
            conversor = ConversorMoneda.obtener_conversor(divisa)
            monto_convertido = conversor.convertir(monto)
            gasto = Gasto(fecha, monto_convertido, divisa, metodo_pago, tipo_gasto)
        elif divisa == TipoMoneda.EUR:
            conversor = ConversorMoneda.obtener_conversor(divisa)
            monto_convertido = conversor.convertir(monto)
            gasto = Gasto(fecha, monto_convertido, divisa, metodo_pago, tipo_gasto)
        else:
            print("La moneda no es válida.")
        self.__viaje_controller.agregar_gasto(gasto)
        # fecha_gasto = datetime.strptime(fecha, '%Y-%m-%d')
        # if not (self.viaje_actual.get_fecha_inicio() <= fecha_gasto <= self.viaje_actual.get_fecha_final()):
        #     print("La fecha del gasto no está dentro del rango del viaje.")
        #     return

        # if monto <= 0:
        #     print("El monto del gasto debe ser mayor que 0.")
        #     return
        # conversor = ConversorMoneda.obtener_conversor(divisa)
        # monto_convertido = conversor.convertir(monto)
        # gasto = Gasto(fecha_gasto, monto_convertido, tipo, metodo_pago, divisa)
        # self.viaje_actual.agregar_gasto(gasto)        
        # # Mostrar la diferencia con el presupuesto diario actualizado
        # print("Gasto agregado con éxito.")
        # print("Diferencia con el presupuesto diario:", self.viaje_actual.mostrar_diferencia_presupuesto())
        # return gasto
        
        



    
# class GestorGastos:
#     def __init__(self):
#         self.gastos = []
#         self.conversor_dolar = ConversorMonedaDolar()
#         self.conversor_euro = ConversorMonedaEuro()

#     def adicionar_gasto(self, fecha, monto, moneda: TipoMoneda, tipo, metodo_pago):
#         gasto = Gasto(fecha, monto, moneda, tipo, metodo_pago)
#         if moneda == TipoMoneda.USD:
#             gasto.monto_pesos = self.conversor_dolar.convertir(monto, moneda.value)
#         elif moneda == TipoMoneda.EUR:
#             gasto.monto_pesos = self.conversor_euro.convertir(monto, moneda.value)
#         else:
#             gasto.monto_pesos = monto
#         self.gastos.append(gasto)
#         return gasto

#     def listar_gastos(self):
#         for gasto in self.gastos:
#             print(f"Fecha: {gasto.fecha}, Monto Original: {gasto.monto_original} {gasto.moneda.value}, "
#                   f"Monto en Pesos: {gasto.monto_pesos}, Tipo: {gasto.tipo}, Método: {gasto.metodo_pago}")
