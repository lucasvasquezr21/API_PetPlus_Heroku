from django.db import models
# Create your models here.

class ReservaHoras(models.Model):
    id_reserva_horas = models.AutoField(primary_key=True)
    horas = models.CharField(max_length=5)
    veterinaria_id_veterinaria_id = models.ForeignKey('app_veterinaria.Veterinaria', models.DO_NOTHING, db_column='veterinaria_id_veterinaria')
    estado_hora_id_estado_hora = models.ForeignKey('app_estado_hora.EstadoHora', models.DO_NOTHING, db_column='estado_hora_id_estado_hora')
    estado_hora = models.CharField(max_length=100)

    
    
    class Meta:
        managed = False
        db_table = 'reserva_horas'

    def __str__(self):
        return f'| Hora: {self.horas} hrs. {self.veterinaria_id_veterinaria_id}| Estado hora: {self.estado_hora_id_estado_hora}|Estado hora: {self.estado_hora} |'

