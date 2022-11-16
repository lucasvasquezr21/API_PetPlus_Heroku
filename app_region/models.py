from django.db import models

# Create your models here.

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return f'{self.nombre_region}'