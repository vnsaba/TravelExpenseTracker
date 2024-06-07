from ..service.conversorMonedaDolar import ConversorMonedaDolar
from ..service.conversorMonedaEuro import ConversorMonedaEuro
from ..enums.TipoMoneda import TipoMoneda

class ConversorMoneda():
    @staticmethod
    def obtener_conversor(moneda):
        if moneda == TipoMoneda.USD:
            return ConversorMonedaDolar()
        elif moneda == TipoMoneda.EUR:
            return ConversorMonedaEuro()
        else:
            raise ValueError("Moneda no soportada")