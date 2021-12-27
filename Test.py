from Servicio import Servicio
from Hospedaje import Hospedaje
from Sistema import Sistema

sistema= Sistema()


sistema.agregarHospedaje(0.56, False, "abc", 12345)
sistema.agregarGastronomia(1.21, True, "def", 67890, 3)


sistema.toString()