from datetime import datetime
from ..enums.TipoMoneda import TipoMoneda
from ..enums.MetodoPago import MetodoPago
from ..enums.TipoGasto import TipoGasto
from ..entity.Gasto import Gasto
from .ControllerConversorMoneda import ControllerConversorMoneda

class GastoController():
    """
    Controlador para gestionar los gastos de un viaje.
    """
    def __init__(self, viaje_controller):
        self.__viaje_controller = viaje_controller
        self.valor = 0

    def verificar_viaje (self):
        """
        Verifica si existe un viaje creado.

        return:
        - True si hay un viaje creado, False de lo contrario.
        """
        if self.__viaje_controller.get_viaje() is None:
            print("Primero debe crear un viaje.")
            return False
        return True
    
    def registrar_gasto(self, fecha: datetime, monto: float,
                       metodo_pago: MetodoPago, tipo_gasto: TipoGasto):
        """
        Registra un nuevo gasto en el viaje.

        params:
               fecha: Fecha del gasto.
               monto: Monto del gasto.
               metodo_pago: Método de pago utilizado.
               tipo_gasto: Tipo de gasto realizado.

        return:
               True si el gasto se registró correctamente, False de lo contrario.
        """
        self.validar_monto(monto)
        tipo_divisa = self.__viaje_controller.divisa()
        if self.verificar_viaje():
            print("Registrando gasto...")
            monto = self.verificar_divisa(tipo_divisa, monto)
            gasto = Gasto(fecha, monto, metodo_pago, tipo_gasto)
            self.valor = monto
            return self.__viaje_controller.adicionar_gasto(gasto)            

    def diferencia_presupuesto(self):
        """
        Calcula la diferencia entre el presupuesto diario del viaje y el  gasto registrado.

        return: La diferencia entre el presupuesto diario y el  gasto registrado.
        """
        return self.__viaje_controller.get_viaje().get_presupuesto_diario() - self.valor
    
    def validar_monto (self, monto):
        """
            Verifica que el monto proporcionado sea no negativo.
            params: monto : El monto a validar.
            Excepciones:
                ValueError: Se lanza si el `monto` proporcionado es menor que cero, indicando que el monto no es válido.
        """
        if monto < 0 :
            raise ValueError("El monto debe ser mayor que cero.")

    def verificar_divisa(self,tipo_divisa, monto):
        if tipo_divisa != TipoMoneda.COP:
                monto = ControllerConversorMoneda.obtener_conversor(tipo_divisa, monto)
        return monto
    
       