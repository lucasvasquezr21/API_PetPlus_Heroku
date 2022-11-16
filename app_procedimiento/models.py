from django.db import models

# Create your models here.

class Procedimiento(models.Model):
    id_procedimiento = models.AutoField(primary_key=True)
    nombre_procedimiento = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procedimiento'

    def __str__(self):
        return f'{self.nombre_procedimiento}'
