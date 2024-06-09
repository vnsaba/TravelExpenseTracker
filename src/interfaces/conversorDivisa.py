from abc import ABC, abstractmethod

class ConversorDivisa(ABC):
    """
        clase abstracta para la conversion de moneda
    """
    @abstractmethod
    def obtener_tasa_conversion(self, tipo_moneda):
        """
            Metodo abstracto para obtener la tasa de conversion de una moneda en especifico

            :param tipo_moneda: El tipo de moneda para el cual se desea obtener la tasa de conversión.
        """
        pass

    @abstractmethod
    def convertir(self, monto, tipo_moneda):
        """
           Método abstracto para convertir una cantidad a una moneda específica.

          :param monto: La cantidad de dinero a convertir.
        """
        pass