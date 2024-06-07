class Gasto:
    def __init__(self, fecha, valor, moneda, metodo_pago, tipo_gasto):
        self._fecha = fecha
        self._valor = valor
        self._moneda = moneda
        self._metodo_pago = metodo_pago
        self._tipo_gasto = tipo_gasto

    # def to_dict(self):
    #     return {
    #         "fecha": self._fecha.strftime('%Y-%m-%d'),
    #         "monto": self._valor,
    #         "tipo": self._tipo_gasto,
    #         "metodo_pago": self._metodo_pago,
    #         "moneda": self._moneda
    #     }

    def getFecha(self):
        return self._fecha

    def getValor(self):
        return self._valor

    def setValor(self, valor):
        self._valor = valor

    def getMoneda(self):
        return self._moneda

    def setMoneda(self, moneda):
        self._moneda = moneda

    def getMetodoPago(self):
        return self._metodo_pago

    def setMetodoPago(self, metodo_pago):
        self._metodo_pago = metodo_pago

    def getTipoGasto(self):
        return self._tipo_gasto

    def setTipoGasto(self, tipo_gasto):
        self._tipo_gasto = tipo_gasto