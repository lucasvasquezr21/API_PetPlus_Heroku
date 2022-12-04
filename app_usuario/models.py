from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=24)
    contrasena = models.CharField(max_length=34)  
    emp_id_emp = models.ForeignKey('app_emp.Emp', models.DO_NOTHING, db_column = 'emp_id_emp')

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return f'{self.usuario} | {self.emp_id_emp}'
