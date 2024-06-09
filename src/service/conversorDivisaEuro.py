import requests
from ..interfaces.conversorDivisa import ConversorDivisa

class ConversorDivisaEuro(ConversorDivisa):
    """
    Clase para realizar conversiones de moneda utilizando un servicio de tasa de cambio.
    """


    def obtener_tasa_conversion(self):
        """
        Obtiene la tasa de conversión actual de EUR a COP utilizando un servicio externo.

        return:
        - La tasa de conversión actual de EUR a COP.
        """
        response = requests.get("https://v6.exchangerate-api.com/v6/26901b9538bf8ff8aeef69b6/pair/EUR/COP")
        tasa = response.json()    
        return tasa['conversion_rate']  

    def convertir(self, monto):
        """
        Convierte un monto dado de EUR a COP utilizando la tasa de conversión actual.

        params: monto: Monto en euros a convertir.

        return: El monto convertido a pesos colombianos.
        """
        rate = self.obtener_tasa_conversion()
        return monto * rate
