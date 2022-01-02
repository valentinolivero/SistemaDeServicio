from Servicio import Servicio
from datetime import date, datetime
from abc import ABCMeta, abstractmethod #libreria para las clases abstractas
dia= date
class Hospedaje(Servicio):
    hospedaje= ""
    precioPorNoche= 0.0

     
    def __init__(self, codServicio, porcentajeDescuento, enPromocion, hospedaje, precioPorNoche):
        super().__init__(codServicio, porcentajeDescuento, enPromocion)
        self.hospedaje= hospedaje
        self.precioPorNoche= precioPorNoche

    def get_hospedaje(self):
        return self.hospedaje
    
    def get_precioPorNoche(self):
        return self.precioPorNoche

    def set_hospedaje(self, hospedaje):
        self.hospedaje=hospedaje

    def set_precioPorNoche(self, precioPorNoche):
        self.precioPorNoche=precioPorNoche
        
                
    def calcularPrecioFinal(self, dia=date):
        
        # //Si está en promoción aplica descuento de lunes a viernes
        precioFinal= self.precioPorNoche
        
        if (self.enPromocion == True and dia.isoweekday()!=6 and dia.isoweekday!=7):
            precioFinal=self.precioPorNoche*(1-(self.porcentajeDescuento/100))
        return precioFinal        
    
    def __str__(self):
        return f'Servicio: -- {super().__str__()} - Hospedaje: {self.hospedaje} - Precio por noche: {self.precioPorNoche}'

    
              

