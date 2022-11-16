import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Estado

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class EstadoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,id_estado=0):
        if (id_estado>0):
            estados=list(Estado.objects.filter(id_estado=id_estado).values())
            if len(estados) > 0:
                estado=estados[0]
                datos={'message':"Success",'estados':estado}
            else:
                datos={'message':"estados no encontrados..."}
            return JsonResponse(datos)
        else:
            estados=list(Estado.objects.values())
            if len(estados)>0:
                datos={'message':"Success",'estados':estados}
            else:
                datos={'message':"estados no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Estado.objects.create(
            estado=jd['estado']      
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_estado):
        jd=json.loads(request.body)
        estados = list(Estado.objects.filter(id_estado=id_estado).values())
        if len(estados) > 0:
            estado=Estado.objects.get(id_estado=id_estado)
            estado.estado=jd['estado']
            estado.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"estado not found"}
        return JsonResponse(datos)



    def delete(self,request, id_estado):
        estados = list(Estado.objects.filter(id_estado=id_estado).values())
        if len(estados) > 0:
            Estado.objects.filter(id_estado=id_estado).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "estado no encontrado"}
        return JsonResponse(datos)