from django.db import models

# Create your models here.

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=45)
    region_id_region = models.ForeignKey('app_region.Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
        return f'{self.nombre_comuna}'