from datetime import datetime
from ..utils.GastoSerializer import GastoSerializer
from ..enums.TipoMoneda import TipoMoneda
from ..entity.Viaje import Viaje

class ViajeSerializer:
    """
    Clase para serializar y deserializar objetos Viaje.
    """

    @staticmethod
    def to_dict(viaje):
        """
        Convierte un objeto Viaje en un diccionario.

        params:
            viaje: Objeto Viaje a serializar.

        return:
            Un diccionario que representa el objeto Viaje serializado.
        """
        return {
            "numero_viaje": viaje.get_numero(),
            "destino": viaje.get_destino(),
            "divisa": viaje.get_divisa().name,  # Asumiendo que divisa es un enum
            "fecha_inicio": viaje.get_fecha_inicio().strftime('%Y-%m-%d %H:%M:%S'),
            "fecha_fin": viaje.get_fecha_final().strftime('%Y-%m-%d %H:%M:%S'),
            "presupuesto_diario": viaje.get_presupuesto_diario(),
            "gastos": [GastoSerializer.to_dict(gasto) for gasto in viaje.get_gastos()] 
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Viaje a partir de un diccionario.

        params:
            data: Diccionario con los datos del objeto Viaje.

        return:
            Un objeto Viaje creado a partir de los datos proporcionados en el diccionario.
        """
        viaje = Viaje(
            data["destino"],
            TipoMoneda[data["divisa"]],
            datetime.strptime(data["fecha_inicio"], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(data["fecha_fin"], "%Y-%m-%d %H:%M:%S"),
            data["presupuesto_diario"]
        )
        gastos = [GastoSerializer.from_dict(gasto_data) for gasto_data in data["gastos"]]
        for gasto in gastos:
            viaje.adicionar_gasto(gasto)
        
        return viaje