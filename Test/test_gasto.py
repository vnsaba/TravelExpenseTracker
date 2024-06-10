
from datetime import datetime
import unittest
from src.enums.TipoGasto import TipoGasto
from src.enums.TipoMoneda import TipoMoneda
from src.enums.MetodoPago import MetodoPago
from src.controller.gastoController import GastoController
from src.controller.viajeController import ViajeController

class TestGasto(unittest.TestCase):

    def setUp(self):
        """Configuración inicial común para todas las pruebas."""
        self.viaje_controller = ViajeController()   
        fecha_inicio = "2024-06-15"
        fecha_inicial = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-20"
        fecha_fimal = datetime.strptime(fecha_fin, "%Y-%m-%d")
        self.viaje_controller.registrar_viaje("Canada", TipoMoneda.USD , fecha_inicial, fecha_fimal, 250.0)
        self.gasto_controller = GastoController(self.viaje_controller)

    def test_datos_correctos(self):
        """Prueba el registro de un gasto con datos correctos."""
        fecha = "2024-06-16"
        fecha_gasto = datetime.strptime(fecha, "%Y-%m-%d")
        resultado = self.gasto_controller.registrar_gasto(fecha_gasto, 100, MetodoPago.EFECTIVO, TipoGasto.ALOJAMIENTO)
        self.assertTrue(resultado)

    def test_monto_negativo(self):
        """Prueba el registro de un gasto con un monto negativo."""
        fecha = "2024-06-16"
        fecha_gasto = datetime.strptime(fecha, "%Y-%m-%d")
        with self.assertRaises(ValueError):
            self.gasto_controller.registrar_gasto(fecha_gasto, -100, MetodoPago.TARJETA, TipoGasto.ENTRETENIMIENTO)

    def test_fecha_fuera_de_rango(self):
        """Prueba el registro de un gasto con la fecha fuera del rango del viaje."""
        fecha = "2024-10-30"
        fecha_gasto = datetime.strptime(fecha, "%Y-%m-%d")
        resultado = self.gasto_controller.registrar_gasto(fecha_gasto, 100, MetodoPago.EFECTIVO, TipoGasto.ALOJAMIENTO)
        self.assertFalse(resultado)