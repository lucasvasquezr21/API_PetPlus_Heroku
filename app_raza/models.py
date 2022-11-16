from django.db import models

# Create your models here.

class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nombre_raza = models.CharField(max_length=45)
    especie_id_especie = models.ForeignKey('app_especie.Especie', models.DO_NOTHING, db_column ='especie_id_especie')


    class Meta:
        managed = False
        db_table = 'raza'

    def __str__(self):
        return f'{self.nombre_raza}'