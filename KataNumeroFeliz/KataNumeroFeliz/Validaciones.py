import Operaciones 

class Validaciones():

    def __init__(self):
        self.operaciones = Operaciones.Operaciones()

    def GetNumeroValido(self, numero):
        return (numero > 0)

    def GetEsFeliz(self, numero):
        if (numero / 10 != 0):
            while (numero / 10 != 0):
                total = 0                   
                resto = numero % 10
                numero = numero /10
                total = total + self.operaciones.GetCuadrado(resto)
            return total + self.operaciones.GetCuadrado(numero)
        else:
            return self.operaciones.GetCuadrado(numero);