import unittest
from datetime import datetime
from src.controller.viajeController import ViajeController
from src.enums.TipoMoneda import TipoMoneda

class TestViaje(unittest.TestCase):
    def test_registro_viaje_normal(self):
        """
        Prueba el registro normal de un viaje con entradas válidas. Verifica si el proceso de
        registro devuelve True, indicando un registro exitoso.
        """
        viaje_controller = ViajeController()
        
        fecha_inicio = "2024-06-15"
        fecha_inicial = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-20"
        fecha_final = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        resultado = viaje_controller.registrar_viaje("Bogotá", TipoMoneda.USD , fecha_inicial, fecha_final, 250.0)
        self.assertTrue(resultado)
    
    def test_fecha_inicio_invalida(self):
        """
        Prueba el registro de un viaje con una fecha de inicio inválida para asegurar que el sistema
        identifique y rechace correctamente los viajes que comienzan antes de la fecha actual.
        """
        viaje_controller = ViajeController()
        
        fecha_inicio = "2024-04-20"
        fecha_inicial = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-20"
        fecha_final = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        resultado = viaje_controller.registrar_viaje("Bogotá", TipoMoneda.USD, fecha_inicial, fecha_final, 150.0)
        self.assertFalse(resultado)
        
    def test_prep_incorrecto(self):
        """
        Prueba el registro de un viaje con una cantidad negativa en el presupuesto. 
        """
        viaje_controller = ViajeController()
        
        fecha_inicio = "2024-06-18"
        fecha_inicial = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = "2024-06-30"
        fecha_final = datetime.strptime(fecha_fin, "%Y-%m-%d")

        with self.assertRaises(ValueError):
            viaje_controller.registrar_viaje("Bogotá", TipoMoneda.EUR, fecha_inicial, fecha_final, -300.0)      
        
