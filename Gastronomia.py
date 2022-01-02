from Servicio import Servicio
from datetime import datetime, date
from abc import ABCMeta, abstractmethod #libreria para las clases abstractas
class Gastronomia(Servicio):
    gastronomia= ""
    precio= 0.0
    diaSemDesc= 0
    def __init__(self, codServicio, porcentajeDescuento, enPromocion, gastronomia, precio, diaSemDesc):
        super().__init__(codServicio, porcentajeDescuento, enPromocion)
        self.gastronomia= gastronomia
        self.precio=precio
        self.diaSemDesc= diaSemDesc
    
    def get_gastronomia(self):
        return self.gastronomia

    def get_precio(self):
        return self.precio

    def get_diaSemDesc(self):
        return self.diaSemDesc

    def set_gastronomia(self, gastronomia):
        self.gastronomia=gastronomia            

    def set_precio(self, precio):
        self.precio=precio

    def set_diaSemDesc(self, diaSemDesc):
        self.diaSemDesc=diaSemDesc

    def calcularPrecioFinal(self, dia):
        #//Si está en promoción aplica el porcentajeDescuento
        precioFinal=self.precio
        
        if (self.enPromocion == True and dia.isoweekday()==self.diaSemDesc):
             #weekday devuelve 6 si es sabado y 7 si es domingo , 1 si es lunes ..., 4 si es viernes
                precioFinal= self.precio*(1-(self.porcentajeDescuento/100))
        
        return precioFinal
    
    def __str__(self):
        return f'Servicio: --  {super().__str__()} - Gastronomia: {self.gastronomia} - Precio: {self.precio} - Dia de la semana de descuento: {self.diaSemDesc}'