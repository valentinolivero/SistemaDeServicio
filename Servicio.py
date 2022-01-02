from abc import ABCMeta, abstractmethod 
from datetime import date
class Servicio(metaclass= ABCMeta):
    codServicio= ""
    porcentajeDescuento= 0.0
    enPromocion= bool
    def __init__(self, codServicio, porcentajeDescuento, enPromocion):
        if (len(codServicio)!=6):
            raise TypeError ("Error, debe contener 6 caracteres el codigo servicio")
        self.codServicio=codServicio
        self.porcentajeDescuento=porcentajeDescuento
        self.enPromocion=enPromocion
    
    def get_codServicio(self):
        return self.codServicio
    
    def get_porcentajeDescuento(self):
        return self.porcentajeDescuento

    def get_enPromocion(self):
        return self.enPromocion
    
    def set_codServicio(self, codServicio):
        self.codServicio=codServicio

    def set_porcentajeDescuento(self, porcentajeDescuento):
        self.porcentajeDescuento=porcentajeDescuento

    def set_enPromocion(self, enPromocion):
        self.enPromocion=enPromocion
        
                
    def __str__(self):
        return f'Codigo: {self.codServicio} - Porcentaje de descuento: {self.porcentajeDescuento} - en promocion: {self.enPromocion}'

    def equalsEnPromocion(self, enPromo):
        return self.enPromocion==enPromo
    
    def equalServicio(self, servicio):
        return servicio.codServicio==self.codServicio and servicio.porcentajeDescuento==self.porcentajeDescuento and servicio.enPromocion ==self.enPromocion 
    @abstractmethod
    def calcularPrecioFinal(self, dia =date):
        pass    