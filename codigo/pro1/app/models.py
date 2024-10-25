from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def vefecha(valor):
    if valor > timezone.now().date():
        raise ValidationError("La fecha de nacimiento no puede ser futura.")

def vedad(valor):
    if valor > 99:
        raise ValidationError("La edad no puede ser mayor que 99.")

class modelo_mas(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField(validators=[vedad])
    fecha_nacimiento = models.DateField(validators=[vefecha])