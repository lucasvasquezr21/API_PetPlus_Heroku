import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import EstadoHora
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class EstadoHoraView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_estado_hora=0):
        if (id_estado_hora>0):
            estados=list(EstadoHora.objects.filter(id_estado_hora=id_estado_hora).values())
            if len(estados) > 0:
                estado=estados[0]
                datos={'message':"Success",'id_estado_hora':estado}
            else:
                datos={'message':"estados no encontrados..."}
            return JsonResponse(datos)
        else:
            estados=list(EstadoHora.objects.values())
            if len(estados)>0:
                datos={'message':"Success",'estados':estados}
            else:
                datos={'message':"Comuunas no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        EstadoHora.objects.create(
            id_estado_hora=jd['id_estado_hora'],
            estado=jd['estado']        
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_estado_hora):
        jd=json.loads(request.body)
        estados = list(EstadoHora.objects.filter(id_estado_hora=id_estado_hora).values())
        if len(estados) > 0:
            estado=EstadoHora.objects.get(id_estado_hora=id_estado_hora)
            estado.estado=jd['estado']
            estado.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"estado not found"}
        return JsonResponse(datos)

    def delete(self,request, id_estado_hora):
        estados = list(EstadoHora.objects.filter(id_estado_hora=id_estado_hora).values())
        if len(estados) > 0:
            EstadoHora.objects.filter(id_estado_hora=id_estado_hora).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Estado hora no encontrado"}
        return JsonResponse(datos)
