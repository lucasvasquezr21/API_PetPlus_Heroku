from django.db import models

# Create your models here.

class ConsultaReserva(models.Model):
    id_consulta_reserva = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=45)      
    
    reserva_horas_id_reserva_horas = models.ForeignKey('app_reserva.ReservaHoras', models.DO_NOTHING, db_column='reserva_horas_id_reserva_horas')
    animal_id_animal = models.ForeignKey('app_animal.Animal', models.DO_NOTHING, db_column='animal_id_animal')

    class Meta:
        managed = False
        db_table = 'consulta_reserva'

    def __str__(self):
        return f'Fecha : {self.fecha}| Mascota: {self.animal_id_animal}| Reserva: {self.reserva_horas_id_reserva_horas}'
