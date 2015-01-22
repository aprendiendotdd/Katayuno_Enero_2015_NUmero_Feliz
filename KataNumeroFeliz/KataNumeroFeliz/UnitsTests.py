import unittest 
from KataNumeroFeliz import *

class Test_KataNumeroFeliz(unittest.TestCase):

    def test_EsNumeroNatural(self):
        validacion = Validaciones()
        resutl = validacion.GetNumeroValido()
        self.assertTrue(result)
    
    #def test_CuadradoDeUnNumero(self):
    #    operaciones = Operaciones()
    #    result = operaciones.GetCuadrado(2)
    #    self.assertEqual(4,result)
    
    #def test_SumaCuadradosDigitos(sefl):
    #    operaciones = Operaciones()
    #    result = operaciones.GetSuma

        


if __name__ == '__main__':
unittest.main()