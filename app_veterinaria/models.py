from django.db import models


# Create your models here.
class Veterinaria(models.Model):
    id_veterinaria = models.AutoField(primary_key=True)
    nombre_vet = models.CharField(max_length=45)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=45)
    correo = models.EmailField('Tu correo electrónico')
    comuna_id_comuna = models.ForeignKey('app_comuna.Comuna', models.DO_NOTHING, db_column='comuna_id_comuna')
    descripcion = models.TextField(max_length=499)
    class Meta:
        managed = False
        db_table = 'veterinaria'

    def __str__(self):
        return f'| Nombre: {self.nombre_vet}'    
