from django.db import models


# Create your models here.

class ConsultaProcedimiento(models.Model):
    id_consulta_procedimiento = models.AutoField(primary_key=True)
    observaciones = models.TextField(max_length=3000)
    emp_id_emp = models.ForeignKey('app_emp.Emp', models.DO_NOTHING, db_column='emp_id_emp')
    procedimiento_id_procedimiento = models.ForeignKey('app_procedimiento.Procedimiento', models.DO_NOTHING, db_column='procedimiento_id_procedimiento')
    consulta_reserva_id_consulta_reserva = models.ForeignKey("app_consulta_reserva.ConsultaReserva", models.DO_NOTHING, db_column='consulta_reserva_id_consulta_reserva')
    motivo_consulta = models.CharField(max_length=45)        
    peso = models.FloatField()
    fecha_pro = models.CharField(max_length=45)      


    class Meta:
        managed = False
        db_table = "consulta_procedimiento"
    
    def __str__(self):
        return f'{self.consulta_reserva_id_consulta_reserva}'
