from ..entity.Reporte import Reporte

class ReporteController ():

    def __init__(self, viaje):
        self.viaje = viaje

    def generar_reporte_diario(self):
        """
        Genera y muestra el reporte diario del viaje.
        """
        reporte = Reporte(self.viaje)
        reporte.reporte_diario()

    def generar_reporte_por_tipo(self):
        """
        Genera y muestra el reporte por tipo de gasto del viaje.
        """
        reporte = Reporte(self.viaje)
        reporte.reporte_por_tipo()