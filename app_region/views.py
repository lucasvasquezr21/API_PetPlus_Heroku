import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Region

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class RegionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id_region=0):
        if (id_region>0):
            regiones=list(Region.objects.filter(id_region=id_region).values())
            if len(regiones) > 0:
                region=regiones[0]
                datos={'message':"Success",'regiones':region}
            else:
                datos={'message':"regiones no encontrados..."}
            return JsonResponse(datos)
        else:
            regiones=list(Region.objects.values())
            if len(regiones)>0:
                datos={'message':"Success",'regiones':regiones}
            else:
                datos={'message':"regiones no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Region.objects.create(
            nombre_region=jd['nombre_region']      
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_region):
        jd=json.loads(request.body)
        regiones = list(Region.objects.filter(id_region=id_region).values())
        if len(regiones) > 0:
            region=Region.objects.get(id_region=id_region)
            region.nombre_region=jd['nombre_region']
            region.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"region not found"}
        return JsonResponse(datos)



    def delete(self,request, id_region):
        regiones = list(Region.objects.filter(id_region=id_region).values())
        if len(regiones) > 0:
            Region.objects.filter(id_region=id_region).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "region no encontrado"}
        return JsonResponse(datos)