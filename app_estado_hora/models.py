from django.db import models

# Create your models here.

class EstadoHora(models.Model):
    id_estado_hora = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'estado_hora'
    
    def __str__(self):
        return f'{self.estado}'
