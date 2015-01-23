import Operaciones 

class Validaciones():

    def __init__(self):
        self.operaciones = Operaciones.Operaciones()

    def GetNumeroValido(self, numero):
        return (numero > 0)

    def GetEsFeliz(self, numero):
        if (numero / 10 != 0):
            return self.operaciones.GetSumaCuadrados(numero)
        else:
            return self.operaciones.GetCuadrado(numero);