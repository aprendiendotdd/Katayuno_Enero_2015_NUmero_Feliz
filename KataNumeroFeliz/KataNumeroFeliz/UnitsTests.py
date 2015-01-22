import unittest 
from Validaciones import *
from Operaciones import *

class Test_KataNumeroFeliz(unittest.TestCase):

    def setUp(self):
        self.validacion = Validaciones()
        return super(Test_KataNumeroFeliz, self).setUp()

    def tearDow(self):
        pass

    def test_EsNumeroEnteroPositivo(self):
        self.assertTrue(self.validacion.GetNumeroValido(1))

    def test_EsFelizSiResultadoEs1(self):
        self.assertEqual(1, self.validacion.GetEsFeliz(1))

    def test_Devuelve_Cuadrado_SI_No_Es_Feliz(self):
        self.assertEqual(4, self.validacion.GetEsFeliz(2))

    def test_Devuelve_Suma_de_Cuadrados_SI_No_Es_Feliz_Un_Numero_De_Dos_digitos(self):
        self.assertEqual(2, self.validacion.GetEsFeliz(11))


    
    #def test_CuadradoDeUnNumero(self):
    #    operaciones = Operaciones()
    #    result = operaciones.GetCuadrado(2)
    #    self.assertEqual(4,result)
    
    #def test_SumaCuadradosDigitos(sefl):
    #    operaciones = Operaciones()
    #    result = operaciones.GetSuma
