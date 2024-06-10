from ..enums.MetodoPago import MetodoPago
from ..enums.TipoGasto import TipoGasto

class Reporte:
    def __init__(self, viaje):
        self.viaje = viaje  

    def reporte_diario(self):
        """Genera y muestra un reporte diario de los gastos del viaje."""
        print(f"Reporte Diario para el Viaje a {self.viaje.get_destino()}")
        gastos_por_fecha = {}
        for gasto in self.viaje.get_gastos():
            fecha = gasto.get_fecha()
            metodo_pago = gasto.get_metodo_pago()  
            valor = gasto.get_valor()

            if fecha not in gastos_por_fecha:
                gastos_por_fecha[fecha] = {MetodoPago.EFECTIVO.value: 0, MetodoPago.TARJETA.value: 0}
            
            gastos_por_fecha[fecha][metodo_pago.value] += valor

        for fecha, pagos in gastos_por_fecha.items():
            total_dia = pagos[MetodoPago.EFECTIVO.value] + pagos[MetodoPago.TARJETA.value]
            print(f"Fecha: {fecha}, {MetodoPago.EFECTIVO.value}: {pagos[MetodoPago.EFECTIVO.value]}, {MetodoPago.TARJETA.value}: {pagos[MetodoPago.TARJETA.value]}, Total: {total_dia}")

    def reporte_por_tipo(self):
        """Genera y muestra un reporte por tipo de gasto del viaje."""
        print(f"Reporte por Tipo de Gasto para el Viaje a {self.viaje.get_destino()}")
        gastos_por_tipo = {}
        for gasto in self.viaje.get_gastos():
            tipo_gasto = gasto.get_tipo_gasto()
            metodo_pago = gasto.get_metodo_pago()
            valor = gasto.get_valor()

            if tipo_gasto not in gastos_por_tipo:
                gastos_por_tipo[tipo_gasto] = {MetodoPago.EFECTIVO.value: 0, MetodoPago.TARJETA.value: 0}
            
            gastos_por_tipo[tipo_gasto][metodo_pago.value] += valor

        for tipo, pagos in gastos_por_tipo.items():
            total_tipo = pagos[MetodoPago.EFECTIVO.value] + pagos[MetodoPago.TARJETA.value]
            print(f"Tipo: {tipo.value}, {MetodoPago.EFECTIVO.value}: {pagos[MetodoPago.EFECTIVO.value]}, {MetodoPago.TARJETA.value}: {pagos[MetodoPago.TARJETA.value]}, Total: {total_tipo}")