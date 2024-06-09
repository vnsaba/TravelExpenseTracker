class Reporte:
    def __init__(self, viaje):
        self.viaje = viaje  

    def reporte_diario(self):
        """
        Genera y muestra un reporte diario de los gastos del viaje.

        El reporte incluye la cantidad total gastada en efectivo y con tarjeta para cada fecha.

        """
        print(f"Reporte Diario para el Viaje a {self.viaje.get_destino()}")
        gastos_por_fecha = {}
        for gasto in self.viaje.get_gastos():
            if gasto.get_fecha() not in gastos_por_fecha:
                gastos_por_fecha[gasto.get_fecha()] = {'efectivo': 0, 'tarjeta': 0}
            if gasto.get_metodo_pago() == 'efectivo':
                gastos_por_fecha[gasto.get_fecha()]['efectivo'] += gasto.get_valor()
            else:
                gastos_por_fecha[gasto.get_fecha()]['tarjeta'] += gasto.get_valor()

        for fecha, pagos in gastos_por_fecha.items():
            print(f"Fecha: {fecha}, Efectivo: {pagos['efectivo']}, Tarjeta: {pagos['tarjeta']}")

    def reporte_por_tipo(self):
        """
        Genera y muestra un reporte por tipo de gasto del viaje.

        El reporte incluye la cantidad total gastada en efectivo y con tarjeta para cada tipo de gasto.

        """
        print(f"Reporte por Tipo de Gasto para el Viaje a {self.viaje.destino}")
        gastos_por_tipo = {}
        for gasto in self.viaje.get_gastos():
            if gasto.get_tipo_gasto() not in gastos_por_tipo:
                gastos_por_tipo[gasto.get_tipo_gasto()] = {'efectivo': 0, 'tarjeta': 0}
            if gasto.get_metodo_pago() == 'efectivo':
                gastos_por_tipo[gasto.get_tipo_gasto()]['efectivo'] += gasto.get_valor()
            else:
                gastos_por_tipo[gasto.get_tipo_gasto()]['tarjeta'] += gasto.get_valor()

        for tipo, pagos in gastos_por_tipo.items():
            print(f"Tipo: {tipo}, Efectivo: {pagos['efectivo']}, Tarjeta: {pagos['tarjeta']}")
