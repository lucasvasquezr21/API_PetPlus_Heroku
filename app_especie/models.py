from django.db import models

# Create your models here.

class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    nombre_especie = models.CharField(max_length=45)
    class Meta:
        managed = False
        db_table = 'especie'

    def __str__(self):
        return f'{self.nombre_especie}'