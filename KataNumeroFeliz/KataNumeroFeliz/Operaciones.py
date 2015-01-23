class Operaciones():
    def GetCuadrado(self, numero):
        return numero * numero

    def GetSumaCuadrados(self, numero):      
        total = 0  
        while (self.GetDigitos(numero)):                             
            total += self.GetCuadrado(self.GetResto(numero))
            numero = self.GetDivisionEntera(numero)
        return total + self.GetCuadrado(numero)

      #recusividad
      #if (self.GetDigitos(numero) == 0):
      #      return total + self.GetCuadrado(numero)
      #  else:
      #      total += self.GetCuadrado(self.GetResto(numero))
      #      self.GetSumaCuadrados(self.GetDivisionEntera(numero), total)


    def GetDigitos(self,numero):
        return (self.GetDivisionEntera(numero) != 0)

    def GetDivisionEntera(self,numero):
        return (numero / 10)

    def GetResto(self,numero):
        return (numero % 10)