from datetime import datetime
from ..enums.TipoGasto import TipoGasto
from ..enums.MetodoPago import MetodoPago
from ..entity.Gasto import Gasto


class GastoSerializer:
    """
    Clase para serializar y deserializar objetos Gasto.
    """

    @staticmethod
    def to_dict(gasto):
        """
        Convierte un objeto Gasto en un diccionario.

        params:
            gasto: Objeto Gasto a serializar.

        return:
            Un diccionario que representa el objeto Gasto serializado.
        """
        return {
            "fecha": gasto.get_fecha().strftime('%Y-%m-%d %H:%M:%S'),
            "valor": gasto.get_valor(),
            "metodo_pago": gasto.get_metodo_pago().name, 
            "tipo_gasto": gasto.get_tipo_gasto().name    
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Gasto a partir de un diccionario.

        params:
            data: Diccionario con los datos del objeto Gasto.

        return:
            Un objeto Gasto creado a partir de los datos proporcionados en el diccionario.
        """
        return Gasto(
            datetime.strptime(data["fecha"], '%Y-%m-%d %H:%M:%S'),
            data["valor"],
            MetodoPago[data["metodo_pago"]], 
            TipoGasto[data["tipo_gasto"]]    
        )