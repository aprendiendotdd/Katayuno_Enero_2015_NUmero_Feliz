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

    def test_Devuelve_Suma_de_Cuadrados_SI_No_Es_Feliz_Un_Numero_De_Mas_De_Un_digito(self):
        self.assertEqual(5, self.validacion.GetEsFeliz(12))
        self.assertEqual(14, self.validacion.GetEsFeliz(123))
        self.assertEqual(4, self.validacion.GetEsFeliz(1111))

    def test_Repetir_hasta_20_veces_para_saber_si_es_feliz():
        self.assertEqual(1, self.validacion.GetEsFeliz(19))