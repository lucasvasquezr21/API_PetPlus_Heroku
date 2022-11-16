import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Comuna

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class ComunaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_comuna=0):
        if (id_comuna>0):
            comunas=list(Comuna.objects.filter(id_comuna=id_comuna).values())
            if len(comunas) > 0:
                comuna=comunas[0]
                datos={'message':"Success",'Comunas':comuna}
            else:
                datos={'message':"Comunas no encontrados..."}
            return JsonResponse(datos)
        else:
            comunas=list(Comuna.objects.values())
            if len(comunas)>0:
                datos={'message':"Success",'comunas':comunas}
            else:
                datos={'message':"Comuunas no encontrados..."}
            return JsonResponse(datos)
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Comuna.objects.create(
            nombre_comuna=jd['nombre_comuna'],
            region_id_region = ['region_id_region'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_comuna):
        jd=json.loads(request.body)
        comunas = list(Comuna.objects.filter(id_comuna=id_comuna).values())
        if len(comunas) > 0:
            comuna=Comuna.objects.get(id_comuna=id_comuna)
            comuna.nombre_comuna=jd['nombre_comuna']
            comuna.region_id_region=jd['region_id_region']
            comuna.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"Comuna not found"}
        return JsonResponse(datos)

    def delete(self,request, id_comuna):
        comunas = list(Comuna.objects.filter(id_comuna=id_comuna).values())
        if len(comunas) > 0:
            Comuna.objects.filter(id_comuna=id_comuna).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Comuna no encontrado"}
        return JsonResponse(datos)