from django.db import models

# Create your models here.

class TipoEmp(models.Model):
    id_tipo_emp = models.AutoField(primary_key=True)
    nombre_tipo_emp = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_emp'

    def __str__(self):
        return f'{self.nombre_tipo_emp}'