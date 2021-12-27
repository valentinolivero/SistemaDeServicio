from abc import ABCMeta, abstractmethod 
from datetime import date
class Servicio(metaclass= ABCMeta):
    codServicio= ""
    porcentajeDescuento= 0.0
    enPromocion= bool
    def __init__(self, codServicio, porcentajeDescuento, enPromocion):
        self.codServicio=codServicio
        self.porcentajeDescuento=porcentajeDescuento
        self.enPromocion=enPromocion
    
    def __str__(self):
        return f'Codigo: {self.codServicio} - Porcentaje de descuento: {self.porcentajeDescuento} - en promocion: {self.enPromocion}'

    
    @abstractmethod
    def calcularPrecioFinal(self, dia =date):
        pass    