from ..service.conversorDivisaEuro import ConversorDivisaEuro
from ..service.conversorDivisaDolar import ConversorDivisaDolar
from ..enums.TipoMoneda import TipoMoneda

class ControllerConversorMoneda():
    """
    Controlador para la conversión de montos en diferentes divisas a la divisa correspondiente.
    """

    @staticmethod
    def obtener_conversor(divisa, monto):
        """
        Convierte un monto de dinero a la divisa especificada.

        Dependiendo de la divisa proporcionada, este método utilizará el servicio de conversión adecuado
        para convertir el monto al valor equivalente en esa divisa.

        Params:
            divisa (TipoMoneda): La divisa a la que se desea convertir el monto.
            monto (float): El monto de dinero que se desea convertir.

        Returns:
            float: El monto convertido a la divisa especificada.
        
        Raises:
            ValueError: Si la divisa proporcionada no es soportada.
        """
        if divisa == TipoMoneda.USD:
            return ConversorDivisaDolar().convertir(monto)
        elif divisa == TipoMoneda.EUR:
            return ConversorDivisaEuro().convertir(monto)
        elif divisa == TipoMoneda.COP:
            return monto  
        else:
            raise ValueError("Divisa no soportada")
