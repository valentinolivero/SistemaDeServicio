from Gastronomia import Gastronomia
from Hospedaje import Hospedaje
from Servicio import Servicio
from datetime import date, time
class Sistema():
    lstServicios=[]
    
         
    def agregarHospedaje(self, porcentajeDescuento, enPromocion, hospedaje,precioPorNoche):
        
        id=len(self.lstServicios)+1
        aux= Hospedaje(str(id), porcentajeDescuento, enPromocion, hospedaje, precioPorNoche)
        return self.lstServicios.append(aux)

    def agregarGastronomia(self, porcentajeDescuento, enPromocion, gastronomia, precio, diaSemDescuento):

        id= len(self.lstServicios)+1
        aux= Gastronomia(str(id), porcentajeDescuento, enPromocion, gastronomia, precio, diaSemDescuento)
        return self.lstServicios.append(aux)
    def toString(self):
        contador=0
        #
        # while contador<= len(self.lstServicios):
        for contador in range(len(self.lstServicios)):
            
            if isinstance(self.lstServicios[contador], Hospedaje):
                print (self.lstServicios[contador])
            else:
                print (self.lstServicios[contador])
             
    
