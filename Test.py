from Servicio import Servicio
from Hospedaje import Hospedaje
from Sistema import Sistema
from datetime import date, datetime
from Gastronomia import Gastronomia


sistema= Sistema()
print ("Test python:")
print ("1:")
#sistema.agregarGastronomia("4892",15.0, True, "Hamburguesa criolla", 180, 4)
sistema.agregarGastronomia("489235",15.0, True, "Hamburguesa criolla", 180, 4)
#sistema.agregarHospedaje("2872", 10.0, True, "Cabaña 3 personas", 1500)
sistema.agregarHospedaje("287282", 10.0, True, "Cabaña 3 personas", 1500)
sistema.toString()
print ("2:")
print (sistema.traerServicio("489235").calcularPrecioFinal(date(2020,10,28)))
print (sistema.traerServicio("287282").calcularPrecioFinal(date(2020,10,28)))

print ("3:")

sistema.agregarGastronomia("858927", 15.0, True, "Milanesa con pure", 350, 3 )
sistema.agregarHospedaje("489259",10.0, True, "Habitacion triple", 2200 )
sistema.agregarGastronomia("182835",20.0, False, "Gaseosa", 120, 3 )
sistema.agregarHospedaje("758972", 15.0, False,"Habitacion simple", 1000)

sistema.toString()

print ("4:")
sistema.traerServicioSiEstaEnPromocion(True)

