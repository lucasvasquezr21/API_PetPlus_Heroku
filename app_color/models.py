from django.db import models

# Create your models here.

class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    color = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'color'

    def __str__(self):
        return f'{self.color}'