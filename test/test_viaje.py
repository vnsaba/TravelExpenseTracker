import unittest
from datetime import datetime
from src.controller.viajeController import ViajeController
from src.enums.TipoMoneda import TipoMoneda

class TestViaje(unittest.TestCase):
    def test_registro_viaje_normal(self):
        viaje_controller = ViajeController()
        
        fecha_inicio = "2024-06-15"
        fechaI = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-20"
        fechaF = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        resultado = viaje_controller.registrar_viaje("Bogotá", TipoMoneda.USD , fechaI, fechaF, 250.0)
        self.assertTrue(resultado)
    
    def test_fecha_inicio_invalida(self):
        viaje_controller = ViajeController()
        
        fecha_inicio = "2024-04-20"
        fechaI = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-20"
        fechaF = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        resultado = viaje_controller.registrar_viaje("Bogotá", TipoMoneda.USD, fechaI, fechaF, 150.0)
        self.assertFalse(resultado)
        
    def test_prep_incorrecto(self):
        viaje_controller = ViajeController()
        
        fecha_inicio = "2024-06-18"
        fechaI = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-30"
        fechaF = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        resultado = viaje_controller.registrar_viaje("Bogotá", TipoMoneda.EUR, fechaI, fechaF, -300.0)

        with self.assertRaises(ValueError):
            viaje_controller.validar_presupuesto(-300.0)
        self.assertFalse(resultado)
        
    
if __name__ == '__main__':
    unittest.main()