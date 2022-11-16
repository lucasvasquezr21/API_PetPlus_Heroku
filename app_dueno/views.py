
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Dueno

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class DuenoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_dueno=0):
        if (id_dueno>0):
            duenos=list(Dueno.objects.filter(id_dueno=id_dueno).values())
            if len(duenos) > 0:
                dueno=duenos[0]
                datos={'message':"Success",'dueno':dueno}
            else:
                datos={'message':"duenos no encontrados..."}
            return JsonResponse(datos)
        else:
            duenos=list(Dueno.objects.values())
            if len(duenos)>0:
                datos={'message':"Success",'dueno':duenos}
            else:
                datos={'message':"dueno no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Dueno.objects.create(
            nombre_completo=jd['nombre_completo'],
            telefono=jd['telefono'],
            correo=jd['correo']
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_dueno):
        jd=json.loads(request.body)
        duenos = list(Dueno.objects.filter(id_dueno=id_dueno).values())
        if len(duenos) > 0:
            dueno=Dueno.objects.get(id_dueno=id_dueno)
            dueno.nombre_completo=jd['nombre_completo']
            dueno.telefono=jd['telefono']
            dueno.correo=jd['correo']
            dueno.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"dueno not found"}
        return JsonResponse(datos)

    def delete(self,request, id_dueno):
        duenos = list(Dueno.objects.filter(id_dueno=id_dueno).values())
        if len(duenos) > 0:
            Dueno.objects.filter(id_dueno=id_dueno).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "dueno no encontrado"}
        return JsonResponse(datos)