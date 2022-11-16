from django.db import models

# Create your models here.

class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'sexo'

    def __str__(self):
        return f'{self.sexo}'