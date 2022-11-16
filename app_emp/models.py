from django.db import models

# Create your models here.


class Emp(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=45)
    veterinaria_id_veterinaria = models.ForeignKey('app_veterinaria.Veterinaria',models.DO_NOTHING, db_column = 'veterinaria_id_veterinaria')
    tipo_empleado_id_tipo_empleado = models.ForeignKey('app_tipo_empleado.TipoEmp',models.DO_NOTHING, db_column = 'tipo_empleado_id_tipo_empleado')
    tipo_emp = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'emp'

    def __str__(self):
        return f'{self.nombre_empleado} | {self.tipo_empleado_id_tipo_empleado}'