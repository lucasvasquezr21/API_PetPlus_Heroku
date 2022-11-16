import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Raza

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class RazaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id_raza=0):
        if (id_raza>0):
            razas=list(Raza.objects.filter(id_raza=id_raza).values())
            if len(razas) > 0:
                raza=razas[0]
                datos={'message':"Success",'razas':raza}
            else:
                datos={'message':"razas no encontrados..."}
            return JsonResponse(datos)
        else:
            razas=list(Raza.objects.values())
            if len(razas)>0:
                datos={'message':"Success",'razas':razas}
            else:
                datos={'message':"raza no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Raza.objects.create(
            nombre_raza=jd['raza'],
            especie_id_especie=jd['especie_id_especie']
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_raza):
        jd=json.loads(request.body)
        razas = list(Raza.objects.filter(id_raza=id_raza).values())
        if len(razas) > 0:
            raza=raza.objects.get(id_raza=id_raza)
            raza.nombre_raza=jd['nombre_raza']
            raza.especie_id_especie= jd['especie_id_especie']
            raza.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"raza not found"}
        return JsonResponse(datos)



    def delete(self,request, id_raza):
        razas = list(Raza.objects.filter(id_raza=id_raza).values())
        if len(razas) > 0:
            Raza.objects.filter(id_raza=id_raza).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "raza no encontrado"}
        return JsonResponse(datos)