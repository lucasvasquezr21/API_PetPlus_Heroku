from django.shortcuts import render

# Create your views here.

import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import ConsultaReserva

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ConsultaReservaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_consulta_reserva=0):
        if (id_consulta_reserva>0):
            consulta_reservas=list(ConsultaReserva.objects.filter(id_consulta_reserva=id_consulta_reserva).values())
            if len(consulta_reservas) > 0:
                consulta_reserva=consulta_reservas[0]
                datos={'message':"Success",'reserva':consulta_reserva}
            else:
                datos={'message':"consulta_reserva no encontrados..."}
            return JsonResponse(datos)
        else:
            consulta_reservas=list(ConsultaReserva.objects.values())
            if len(consulta_reservas)>0:
                datos={'message':"Success",'consulta_reserva':consulta_reservas}
            else:
                datos={'message':"consulta_reserva no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd=json.loads(request.body)
        ConsultaReserva.objects.create(
            fecha=jd['fecha'],
         
            reserva_horas_id_reserva_horas_id=jd['reserva_horas_id_reserva_horas_id'],
            animal_id_animal_id=jd['animal_id_animal_id']
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_consulta_reserva):
        jd=json.loads(request.body)
        consulta_reservas = list(ConsultaReserva.objects.filter(id_consulta_reserva=id_consulta_reserva).values())
        if len(consulta_reservas) > 0:
            consulta_reserva=ConsultaReserva.objects.get(id_consulta_reserva=id_consulta_reserva)
            consulta_reserva.fecha=jd['fecha']
            consulta_reserva.save()
            datos = {'mesage':"Success"}
        else:
            datos = {'message':"consulta_reserva not found"}
        return JsonResponse(datos)

    def delete(self,request, id_consulta_reserva):
        consulta_reservas = list(ConsultaReserva.objects.filter(id_consulta_reserva=id_consulta_reserva).values())
        if len(consulta_reservas) > 0:
            ConsultaReserva.objects.filter(id_consulta_reserva=id_consulta_reserva).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "consulta_reserva no encontrado"}
        return JsonResponse(datos) 