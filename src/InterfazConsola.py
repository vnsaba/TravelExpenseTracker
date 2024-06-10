from datetime import datetime
from .controller.gastoController import GastoController
from .controller.viajeController import ViajeController
from .controller.ReporteController import ReporteController
from .enums.TipoGasto import TipoGasto
from .enums.MetodoPago import MetodoPago
from .enums.TipoMoneda import TipoMoneda

class InterfazConsola():
    def __init__(self):
        self.viaje_existe = False
        self.viaje_controller = ViajeController()
        self.gasto_controller = GastoController(self.viaje_controller)

    def formulario_crear_viaje(self):
        """Permite al usuario crear un nuevo viaje"""
        destino = input("Ingrese el destino del viaje: ")
        fecha_inicio = self._ingresar_fecha("Ingrese la fecha de inicio del viaje (YYYY-MM-DD): ")
        fecha_fin = self._ingresar_fecha("Ingrese la fecha de fin del viaje (YYYY-MM-DD): ")
        presupuesto = self._ingresar_valor("Ingrese el presupuesto diario del viaje: ")
        divisa = self._seleccionar_opcion("Monedas disponibles:", TipoMoneda)

        self.guardar_viaje(destino, divisa, fecha_inicio, fecha_fin, presupuesto)

    def guardar_viaje (self, destino, divisa, fecha_inicio, fecha_fin, presupuesto_diario):
        """
            Registra un nuevo viaje con los detalles proporcionados.

            params:
                destino (str): Nombre del destino del viaje.
                divisa (TipoDivisa): Tipo de divisa en la que se manejará el presupuesto del viaje.
                fecha_inicio (datetime): Fecha de inicio del viaje.
                fecha_fin (datetime): Fecha de finalización del viaje.
                presupuesto_diario (float): Presupuesto diario asignado para el viaje.
        """
        viaje_creado = self.viaje_controller.registrar_viaje(destino, divisa, fecha_inicio, fecha_fin, presupuesto_diario)
        if viaje_creado:
            print("¡Buen viaje!")
            self.viaje_existe = True
            self.mostrar_menu_viaje_creado()
        else:
            print("El viaje no pudo ser registrado debido a errores en las fechas o el destino.")
            
    def formulario_crear_gasto(self):
        """Permite al usuario agregar un gasto al viaje actualmente activo"""
        if self.viaje_existe is False:
            print("Primero debe crear un viaje")
            return

        fecha = self._ingresar_fecha("Ingrese la fecha del gasto (YYYY-MM-DD): ")
        valor = self._ingresar_valor("Ingrese el valor del gasto: ")
        tipo = self._seleccionar_opcion("Tipo de gastos disponibles:", TipoGasto)
        metodo_pago = self._seleccionar_opcion("Métodos de pago disponibles:", MetodoPago)
        self.guardar_gasto(fecha, valor, metodo_pago, tipo)    

    def guardar_gasto (self, fecha, valor, metodo_pago, tipo_gasto ):
        """
        Registra un nuevo gasto con los detalles proporcionados.

        params:
            fecha (datetime): Fecha en la que se realizó el gasto.
            valor (float): Monto del gasto.
            metodo_pago (MetodoPago): Método de pago utilizado para el gasto.
            tipo_gasto (TipoGasto): Tipo de gasto realizado.

        """
        gasto_creado =  self.gasto_controller.registrar_gasto(fecha, valor, metodo_pago, tipo_gasto)
        if gasto_creado:
            print("Gasto agregado con éxito.")
            print("Diferencia con el presupuesto diario:", self.gasto_controller.diferencia_presupuesto())
        else:
            print("Ha ocurrido un error al crear el gasto")
        

    def _ingresar_fecha(self, mensaje):
        """
        Solicita al usuario ingresar una fecha en el formato especificado.

        params:
            mensaje (str): Mensaje que indica al usuario qué debe ingresar.

        Returns:
            datetime: Objeto datetime que representa la fecha ingresada por el usuario.
        """
        while True:
            fecha_str = input(mensaje)
            try:
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
                return fecha
            except ValueError:
                print("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato YYYY-MM-DD.")

    def _ingresar_valor(self, mensaje):
        """
        Solicita al usuario ingresar un valor numérico.

        params:
            mensaje (str): Mensaje que indica al usuario qué debe ingresar.

        Returns:
            float: Valor numérico ingresado por el usuario.
        """
        while True:
            valor_str = input(mensaje)
            try:
                valor = float(valor_str)
                return valor
            except ValueError:
                print("Valor incorrecto. Por favor, ingrese un número válido.")

    def _seleccionar_opcion(self, mensaje, opciones_enum):
        """
        Muestra las opciones disponibles y permite al usuario seleccionar una.

        param:
            mensaje (str): Mensaje que indica al usuario qué debe seleccionar.
            opciones_enum (Enum): Enumeración que contiene las opciones disponibles.

        Returns:
            Enum: Opción seleccionada por el usuario.
        """
        opciones = list(opciones_enum)
        print(mensaje)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion.value}")
        while True:
            opcion_idx = int(input("Seleccione una opción (ingrese el número correspondiente): "))
            if opcion_idx in range(1, len(opciones) + 1):
                return opciones[opcion_idx - 1]
            else:
                print("Selección no válida. Por favor, ingrese un número dentro del rango.")

    def salir(self):
        """Guarda la información del viaje en el archivo antes de salir de la aplicación."""
        if self.viaje_controller.guardar_viajes_en_archivo():
            print("¡La información del viaje se ha guardado correctamente!")
            self.mostrar_menu_reporte()
        else:
            print("Error al guardar la información del viaje en el archivo.")
    
    def mostrar_menu(self):
        """Muestra el menú principal de la aplicación de viajes."""
        while True:
            print("\nMenu de la aplicación")
            print("1. Crear un nuevo viaje")
            print("2. Ver historial de viajes")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.formulario_crear_viaje()
            elif opcion == "2":
                self.viaje_controller.lista_viajes()
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")

    def mostrar_menu_viaje_creado(self):
        """ Muestra el menú principal para la aplicación de registro de gastos de viaje."""
        while True:
            print("\nMenu de la aplicación de registro de gastos de viaje")
            print("1. Añadir un gasto")
            print("2. Finalizar viaje")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.formulario_crear_gasto()
            elif opcion == "2":
                self.salir()
                print("Finalizando viaje")
                exit(0)
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 2.")
    
    def mostrar_menu_reporte(self):
        """Muestra un menú interactivo para seleccionar y generar diferentes tipos de reportes de gastos."""
        reporte = ReporteController(self.viaje_controller.get_viaje())
        while True:
            opcion = input("¿Qué reporte desea ver? (Ingrese el número correspondiente):\n"
                                    "1. Reporte diario\n"
                                    "2. Reporte por tipo de gasto\n"
                                    "3. Volver al inicio\n"
                                    "Seleccione una opción: ")
            if opcion == "1":
                reporte.generar_reporte_diario()
            elif opcion == "2":
                reporte.generar_reporte_por_tipo()
            elif opcion == "3":
                self.mostrar_menu()
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
            
