import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Procedimiento
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class ProcedimientoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_procedimiento=0):
            if (id_procedimiento>0):
                procedimientos=list(Procedimiento.objects.filter(id_procedimiento=id_procedimiento).values())
                if len(procedimientos) > 0:
                    procedimiento=procedimientos[0]
                    datos={'message':"Success",'id_procedimiento':procedimiento}
                else:
                    datos={'message':"procedimientos no encontrados..."}
                return JsonResponse(datos)
            else:
                procedimientos=list(Procedimiento.objects.values())
                if len(procedimientos)>0:
                    datos={'message':"Success",'procedimientos':procedimientos}
                else:
                    datos={'message':"Procedimientos no encontrados..."}
                return JsonResponse(datos)
            
    def post(self, request):
            #print(request.body)
            jd=json.loads(request.body)
            #print(jd)
            Procedimiento.objects.create(
                nombre_procedimiento=jd['nombre_procedimiento'],
                descripcion = jd['descripcion'],
                )
            datos={'message':"Success"}
            return JsonResponse(datos)

    def put(self,request,id_procedimiento):
            jd=json.loads(request.body)
            procedimientos = list(Procedimiento.objects.filter(id_procedimiento=id_procedimiento).values())
            if len(procedimientos) > 0:
                procedimiento=Procedimiento.objects.get(id_procedimiento=id_procedimiento)
                procedimiento.nombre_procedimiento=jd['nombre_procedimiento']
                procedimiento.descripcion=jd['descripcion']
                procedimiento.save()
                datos = {'mesage':"Succes"}
            else:
                datos = {'message':"procedimiento not found"}
            return JsonResponse(datos)

    def delete(self,request, id_procedimiento):
            procedimientos = list(Procedimiento.objects.filter(id_procedimiento=id_procedimiento).values())
            if len(procedimientos) > 0:
                Procedimiento.objects.filter(id_procedimiento=id_procedimiento).delete()
                datos = {'message' : "succes"}
            else:
                datos = {'message' : "procedimiento no encontrado"}
            return JsonResponse(datos)
