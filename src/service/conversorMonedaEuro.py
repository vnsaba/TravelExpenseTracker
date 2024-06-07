import requests
from ..interfaces.conversorMoneda import ConversorMoneda

class ConversorMonedaEuro(ConversorMoneda):
    
    def obtener_tasa_conversion(self):
        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
        tasa = response.json()[0]['random'] + 200    
        return tasa  

    def convertir(self, monto):
        tasa = self.obtener_tasa_conversion()
        return monto * tasa
