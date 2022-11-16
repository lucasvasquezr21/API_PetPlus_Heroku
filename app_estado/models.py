from django.db import models

# Create your models here.

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'estado'

    def __str__(self):
        return f'{self.estado}'