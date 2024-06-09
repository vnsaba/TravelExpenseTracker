import requests
from ..interfaces.conversorDivisa import ConversorDivisa

class ConversorDivisaDolar(ConversorDivisa):
    """Clase para convertir divisas a dólares."""
    def obtener_tasa_conversion(self):
        """
        Obtiene la tasa de conversión actual de USD a COP utilizando un servicio externo.

        return: La tasa de conversión actual de USD a COP.
        """
        response = requests.get("https://v6.exchangerate-api.com/v6/26901b9538bf8ff8aeef69b6/pair/USD/COP")
        tasa = response.json()
        return tasa['conversion_rate']

    def convertir(self, monto):
        """
        Convierte un monto dado de USD a COP utilizando la tasa de conversión actual.

        params: monto: Monto en dólares a convertir.

        return: El monto convertido a pesos colombianos.

        """
        rate = self.obtener_tasa_conversion()
        return monto * rate
