import requests
from interfaces.ConversorMoneda import ConversorMoneda

class ConversorMonedaEuro(ConversorMoneda):
    
    def obtener_tasa_conversion(self):
        response = requests.get("https://v6.exchangerate-api.com/v6/26901b9538bf8ff8aeef69b6/pair/EUR/COP")
        tasa = response.json()    
        return tasa['conversion_rate']  

    def convertir(self, monto):
        rate = self.obtener_tasa_conversion()
        return monto * rate
