from Servicio import Servicio
from datetime import date
from abc import ABCMeta, abstractmethod #libreria para las clases abstractas
class Gastronomia(Servicio):
    gastronomia= ""
    precio= 0.0
    diaSemDescuento= 0
    def __init__(self, codServicio, porcentajeDescuento, enPromocion, gastronomia, precio, diaSemDescuento):
        super().__init__(codServicio, porcentajeDescuento, enPromocion)
        self.gastronomia= gastronomia
        self.precio=precio
        self.diaSemDescuento= diaSemDescuento

    def calcularPrecioFinal(self, dia= date):
        return "hola"
    
    def __str__(self):
        return f'Servicio: --  {super().__str__()} - Gastronomia: {self.gastronomia} - Precio: {self.precio} - Dia de la semana de descuento: {self.diaSemDescuento}'