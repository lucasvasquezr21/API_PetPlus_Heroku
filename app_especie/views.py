import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Especie

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class EspecieView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_especie=0):
        if (id_especie>0):
            especies=list(Especie.objects.filter(id_especie=id_especie).values())
            if len(especies) > 0:
                especie=especies[0]
                datos={'message':"Success",'especies':especie}
            else:
                datos={'message':"especies no encontrados..."}
            return JsonResponse(datos)
        else:
            especies=list(Especie.objects.values())
            if len(especies)>0:
                datos={'message':"Success",'especies':especies}
            else:
                datos={'message':"especie no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Especie.objects.create(
            nombre_especie=jd['nombre_especie'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_especie):
        jd=json.loads(request.body)
        especies = list(Especie.objects.filter(id_especie=id_especie).values())
        if len(especies) > 0:
            especie=Especie.objects.get(id_especie=id_especie)
            especie.nombre_especie=jd['nombre_especie']
            especie.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"especie not found"}
        return JsonResponse(datos)



    def delete(self,request, id_especie):
        especies = list(Especie.objects.filter(id_especie=id_especie).values())
        if len(especies) > 0:
            Especie.objects.filter(id_especie=id_especie).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "especie no encontrado"}
        return JsonResponse(datos)