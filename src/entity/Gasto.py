from datetime import datetime
from ..enums.MetodoPago import MetodoPago
from ..enums.TipoGasto import TipoGasto

class Gasto():
    def __init__(self, fecha: datetime, valor: float, 
                 metodo_pago: MetodoPago, tipo_gasto: TipoGasto):
        self.__fecha = fecha
        self.__valor = valor
        self.__metodo_pago = metodo_pago
        self.__tipo_gasto = tipo_gasto

    def get_fecha(self):
        return self.__fecha

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_metodo_pago(self):
        return self.__metodo_pago

    def set_metodo_pago(self, metodo_pago):
        self.__metodo_pago = metodo_pago

    def get_tipo_gasto(self):
        return self.__tipo_gasto

    def set_tipo_gasto(self, tipo_gasto):
        self.__tipo_gasto = tipo_gasto

