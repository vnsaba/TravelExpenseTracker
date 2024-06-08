from entity.Viaje import Viaje
from entity.Gasto import Gasto
from controller.GastoController import GastoController
from controller.ViajeController import ViajeController
class InterfazConsola():
    def __init__(self):
        self.viaje = None
        self.gasto_controller = GastoController()
        self.viaje_controller = ViajeController()


    def añadir_gasto_a_viaje(self):
        if self.viaje is None:
            print("Primero debe crear un viaje.")
            return

        fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
        valor = float(input("Ingrese el valor del gasto: "))

        # Opciones predefinidas para el tipo de gasto
        tipo_gastos = ["transporte", "alojamiento", "alimentación", "entretenimiento", "compras"]
        print("Tipo de gastos disponibles:")
        for i, tipo in enumerate(tipo_gastos, 1):
            print(f"{i}. {tipo}")
        tipo_idx = int(input("Seleccione el tipo de gasto (ingrese el número correspondiente): "))
        while tipo_idx not in range(1, len(tipo_gastos) + 1):
            print("Selección no válida. Por favor, ingrese un número dentro del rango.")
            tipo_idx = int(input("Seleccione el tipo de gasto (ingrese el número correspondiente): "))
        tipo = tipo_gastos[tipo_idx - 1]

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
        for i, divisa in enumerate(monedas, 1):
            print(f"{i}. {divisa}")
        moneda_idx = int(input("Seleccione la moneda del gasto (ingrese el número correspondiente): "))
        while moneda_idx not in range(1, len(monedas) + 1):
            print("Selección no válida. Por favor, ingrese un número dentro del rango.")
            moneda_idx = int(input("Seleccione la moneda del gasto (ingrese el número correspondiente): "))
        divisa = monedas[moneda_idx - 1]

        self.gasto_controller.registrar_gasto(fecha, valor, tipo, metodo_pago, divisa)
        
        def crear_viaje(self):
            numero = str(input("Ingrese el número del viaje: "))
            destino = input("Ingrese el destino del viaje: ")
            fecha_inicio = input("Ingrese la fecha de inicio del viaje (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin del viaje (YYYY-MM-DD): ")
            presupuesto = input("Ingrese el presupuesto diario del viaje: ")
            divisa = (input("Ingrese la moneda del presupuesto: ")).upper()
            self.viaje = Viaje(numero, destino, divisa, fecha_inicio, fecha_fin, presupuesto)
            self.viaje_controller.registrar_viaje(numero, destino, divisa, fecha_inicio, fecha_fin, presupuesto)

  
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
