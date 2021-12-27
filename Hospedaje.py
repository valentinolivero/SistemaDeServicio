from Servicio import Servicio
from datetime import date
from abc import ABCMeta, abstractmethod #libreria para las clases abstractas

class Hospedaje(Servicio):
    hospedaje= ""
    precioPorNoche= 0.0
     
    def __init__(self, codServicio, porcentajeDescuento, enPromocion, hospedaje, precioPorNoche):
        super().__init__(codServicio, porcentajeDescuento, enPromocion)
        self.hospedaje= hospedaje
        self.precioPorNoche= precioPorNoche

    def calcularPrecioFinal(self, dia= date):
        return "hola"

    def __str__(self):
        return f'Servicio: -- {super().__str__()} - Hospedaje: {self.hospedaje} - Precio por noche: {self.precioPorNoche}'

    
              

