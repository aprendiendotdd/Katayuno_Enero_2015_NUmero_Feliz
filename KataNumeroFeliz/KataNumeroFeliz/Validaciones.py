import Operaciones 

class Validaciones():

    def __init__(self):
        self.operaciones = Operaciones.Operaciones()

    def GetNumeroValido(self, numero):
        return (numero > 0)

    def GetEsFeliz(self, numero):        
         return (self.GetCalculoEsFeliz(numero) == 1)

    def GetFinaliceCalculo(self, iteracion, numero):
        return (iteracion == 20) and (numero == 1)

    def GetCalculoEsFeliz(self, numero):           
        iteracion = 0
        while (not self.GetFinaliceCalculo(iteracion, numero)):
            iteracion += 1
            numero = self.operaciones.GetSumaCuadrados(numero)
        return numero
              
            