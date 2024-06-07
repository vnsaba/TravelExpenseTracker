from .entity.Viaje import Viaje
from .entity.Gasto import Gasto
from .controller.gastoController import GastoController
class InterfazConsola:
    def __init__(self):
        self.viaje = None
        self.gasto_controller = None


    def añadir_gasto_a_viaje(self):
        if self.viaje is None:
            print("Primero debe crear un viaje.")
            return

        fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
        valor = float(input("Ingrese el valor del gasto: "))

        # Opciones predefinidas para el tipo de gasto
        tipos_gasto = ["transporte", "alojamiento", "alimentación", "entretenimiento", "compras"]
        print("Tipos de gasto disponibles:")
        for i, tipo in enumerate(tipos_gasto, 1):
            print(f"{i}. {tipo}")
        tipo_idx = int(input("Seleccione el tipo de gasto (ingrese el número correspondiente): "))
        while tipo_idx not in range(1, len(tipos_gasto) + 1):
            print("Selección no válida. Por favor, ingrese un número dentro del rango.")
            tipo_idx = int(input("Seleccione el tipo de gasto (ingrese el número correspondiente): "))
        tipo = tipos_gasto[tipo_idx - 1]

        # Opciones predefinidas para el método de pago
        metodos_pago = ["efectivo", "tarjeta"]
        print("Métodos de pago disponibles:")
        for i, metodo in enumerate(metodos_pago, 1):
            print(f"{i}. {metodo}")
        metodo_idx = int(input("Seleccione el método de pago (ingrese el número correspondiente): "))
        while metodo_idx not in range(1, len(metodos_pago) + 1):
            print("Selección no válida. Por favor, ingrese un número dentro del rango.")
            metodo_idx = int(input("Seleccione el método de pago (ingrese el número correspondiente): "))
        metodo_pago = metodos_pago[metodo_idx - 1]

        # Opciones predefinidas para la moneda
        monedas = ["USD", "EUR", "COP"]
        print("Monedas disponibles:")
        for i, moneda in enumerate(monedas, 1):
            print(f"{i}. {moneda}")
        moneda_idx = int(input("Seleccione la moneda del gasto (ingrese el número correspondiente): "))
        while moneda_idx not in range(1, len(monedas) + 1):
            print("Selección no válida. Por favor, ingrese un número dentro del rango.")
            moneda_idx = int(input("Seleccione la moneda del gasto (ingrese el número correspondiente): "))
        moneda = monedas[moneda_idx - 1]

        self.gasto_controller.registrar_gasto(fecha, valor, tipo, metodo_pago, moneda)

  
    def mostrar_menu(self):
        while True:
            print("\nMenu de la aplicación de registro de gastos de viaje")
            print("1. Crear un nuevo viaje")
            print("2. Añadir un gasto")
            print("3. Ver reporte diario")
            print("4. Ver reporte por tipo de gasto")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
              #  self.crear_viaje()
                pass
            elif opcion == "2":
                self.añadir_gasto_a_viaje()

            elif opcion == "3":
              #  self.mostrar_reporte_diario()
              print("no hay")

            elif opcion == "4":
              #  self.mostrar_reporte_por_tipo()
                print('no hay')
            elif opcion == "5":
                print("Saliendo de la aplicación. ¡Buen viaje!")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
