
from Gastronomia import Gastronomia
from Hospedaje import Hospedaje
from Servicio import Servicio
from datetime import date, time
class Sistema():
    lstServicios=[]
    
         
    def agregarHospedaje(self, codservicio,porcentajeDescuento, enPromocion, hospedaje,precioPorNoche):
        
        aux= Hospedaje(codservicio, porcentajeDescuento, enPromocion, hospedaje, precioPorNoche)
        i=0
        while (i<len(self.lstServicios)):
            if(self.lstServicios[i].equalServicio(aux)):
                 raise TypeError ("Error, ese servicio ya se encuentra en la lista")
            i=i+1
        
        return self.lstServicios.append(aux)

    def agregarGastronomia(self,codServicio, porcentajeDescuento, enPromocion, gastronomia, precio, diaSemDescuento):

        aux= Gastronomia(codServicio, porcentajeDescuento, enPromocion, gastronomia, precio, diaSemDescuento)
        i=0
        while (i<len(self.lstServicios)):
            if(self.lstServicios[i].equalServicio(aux)):
                 raise TypeError ("Error, ese servicio ya se encuentra en la lista")
            i=i+1
        
        return self.lstServicios.append(aux)
    
    
    def toString(self):
        contador=0
      
        while contador<len(self.lstServicios):
            
            if isinstance(self.lstServicios[contador], Hospedaje):
                print (self.lstServicios[contador])
            else:
                print (self.lstServicios[contador])
            contador=contador+1        

    def traerServicio(self, codServicio):
        flag=False
        i=0
        aux= None
        while (len(self.lstServicios)>i and flag==False):
            if  (self.lstServicios[i]).codServicio == codServicio:
                     aux= self.lstServicios[i] 
                     flag=True
            i=i+1       
        return aux
    
    def traerServicioSiEstaEnPromocion (self, enPromocion):
       
        tamanio=len(self.lstServicios)
        aux=[]
        i=0
    
        for i in range(tamanio):
            if self.lstServicios[i].enPromocion==enPromocion:
                aux.append(self.lstServicios[i])
            
        for i in range(len(aux)):            
            if isinstance(aux[i], Hospedaje):
                print (aux[i])
            else:
                print (aux[i])
            
        
        
        
            
            
           
        
    