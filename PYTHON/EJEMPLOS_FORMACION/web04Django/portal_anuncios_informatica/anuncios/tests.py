from django.test import TestCase
from . import models

# Create your tests here.
class TestRegistroAnuncio(TestCase):
    def setUp(self):
        print("preparar registros que luego no se tengan en cuenta")
        models.Usuario.objects.create(nombre="pruebas",email="rueba@gmail.com", clave="123")
        
    def test_registro_usuario(self):
        usuario = models.Usuario.objects.get(email = "prueba@gmail.com")
        self.assertEqual(usuario.email, "prueba@gmail.com")
        