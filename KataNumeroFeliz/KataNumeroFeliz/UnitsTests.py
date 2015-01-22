import unittest 
from Validaciones import *
from Operaciones import *

class Test_KataNumeroFeliz(unittest.TestCase):

    def test_EsNumeroEnteroPositivo(self):
        validacion = Validaciones()
        result = validacion.GetNumeroValido(1)
        self.assertTrue(result)
    
    #def test_CuadradoDeUnNumero(self):
    #    operaciones = Operaciones()
    #    result = operaciones.GetCuadrado(2)
    #    self.assertEqual(4,result)
    
    #def test_SumaCuadradosDigitos(sefl):
    #    operaciones = Operaciones()
    #    result = operaciones.GetSuma
