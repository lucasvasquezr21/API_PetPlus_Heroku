import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import ConsultaProcedimiento

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ConsultaProcedimientoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_consulta_procedimiento=0):
        if (id_consulta_procedimiento>0):
            consulta_procedimientos=list(ConsultaProcedimiento.objects.filter(id_consulta_procedimiento=id_consulta_procedimiento).values())
            if len(consulta_procedimientos) > 0:
                consulta_procedimiento=consulta_procedimientos[0]
                datos={'message':"Success",'consulta_procedimiento':consulta_procedimiento}
            else:
                datos={'message':"consulta_procedimiento no encontrados..."}
            return JsonResponse(datos)
        else:
            consulta_procedimientos=list(ConsultaProcedimiento.objects.values())
            if len(consulta_procedimientos)>0:
                datos={'message':"Success",'consulta_procedimientos':consulta_procedimientos}
            else:
                datos={'message':"consulta_procedimiento no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        ConsultaProcedimiento.objects.create(
            observaciones=jd['observaciones'],
            emp_id_emp_id=jd['emp_id_emp_id'],
            procedimiento_id_procedimiento_id=jd['procedimiento_id_procedimiento_id'],
            consulta_reserva_id_consulta_reserva_id=jd['consulta_reserva_id_consulta_reserva_id'],
            motivo_consulta=jd['motivo_consulta'],
            peso=jd['peso'],
            fecha_pro=jd['fecha_pro'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_consulta_procedimiento):
        jd=json.loads(request.body)
        consulta_procedimientos = list(ConsultaProcedimiento.objects.filter(id_consulta_procedimiento=id_consulta_procedimiento).values())
        if len(consulta_procedimientos) > 0:
            consulta_procedimiento=ConsultaProcedimiento.objects.get(id_consulta_procedimiento=id_consulta_procedimiento)
            consulta_procedimiento.observaciones=jd['observaciones']
            consulta_procedimiento.emp_id_emp=jd['emp_id_emp']
            consulta_procedimiento.procedimiento_id_procedimiento=jd['procedimiento_id_procedimiento']
            consulta_procedimiento.id_consulta_consulta_reserva=jd['consulta_reserva_id_consulta_reserva']
            consulta_procedimiento.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Procedimiento not found"}
        return JsonResponse(datos)

    def delete(self,request, id_consulta_procedimiento):
        consulta_procedimientos = list(ConsultaProcedimiento.objects.filter(id_consulta_procedimiento=id_consulta_procedimiento).values())
        if len(consulta_procedimientos) > 0:
            ConsultaProcedimiento.objects.filter(id_consulta_procedimiento=id_consulta_procedimiento).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Procedimiento no encontrado"}
        return JsonResponse(datos) 