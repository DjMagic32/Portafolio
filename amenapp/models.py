from django.db import models

# Create your models here.
class Contacto (models.Model):

    Nombre_y_Apellido = models.CharField(max_length=50)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=50)
    Mensaje = models.CharField(max_length=400)

