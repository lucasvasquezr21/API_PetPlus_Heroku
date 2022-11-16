import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Sexo

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class SexoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id_sexo=0):
        if (id_sexo>0):
            sexos=list(Sexo.objects.filter(id_sexo=id_sexo).values())
            if len(sexos) > 0:
                sexo=sexos[0]
                datos={'message':"Success",'sexos':sexo}
            else:
                datos={'message':"sexos no encontrados..."}
            return JsonResponse(datos)
        else:
            sexos=list(Sexo.objects.values())
            if len(sexos)>0:
                datos={'message':"Success",'sexos':sexos}
            else:
                datos={'message':"sexos no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Sexo.objects.create(
            sexo=jd['sexo']      
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_sexo):
        jd=json.loads(request.body)
        sexos = list(Sexo.objects.filter(id_sexo=id_sexo).values())
        if len(sexos) > 0:
            sexo=Sexo.objects.get(id_sexo=id_sexo)
            sexo.sexo=jd['sexo']
            sexo.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"sexo not found"}
        return JsonResponse(datos)



    def delete(self,request, id_sexo):
        sexos = list(Sexo.objects.filter(id_sexo=id_sexo).values())
        if len(sexos) > 0:
            Sexo.objects.filter(id_sexo=id_sexo).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "sexo no encontrado"}
        return JsonResponse(datos)