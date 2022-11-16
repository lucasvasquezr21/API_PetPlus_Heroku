from turtle import color
from django.db import models

# Create your models here.

class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)      
    n_microchip = models.CharField(max_length=45, blank=True, null=True)
    dueno_id_dueno = models.ForeignKey('app_dueno.Dueno', models.DO_NOTHING, db_column='dueno_id_dueno')
    color_id_color = models.ForeignKey('app_color.Color', models.DO_NOTHING, db_column='color_id_color')
    especie_id_especie = models.ForeignKey('app_especie.Especie', models.DO_NOTHING, db_column='especie_id_especie')
    estado_id_estado = models.ForeignKey('app_estado.Estado', models.DO_NOTHING, db_column ='estado_id_estado')
    sexo_id_sexo = models.ForeignKey('app_sexo.Sexo', models.DO_NOTHING, db_column = 'sexo_id_sexo')
    tipo_sangre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal'

    def __str__(self):
        return f'{self.nombre} | Dueño: {self.dueno_id_dueno} | Ficha N°: {self.id_animal}'

