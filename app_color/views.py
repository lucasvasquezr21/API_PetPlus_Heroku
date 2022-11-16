import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Color

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class ColorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id_color=0):
        if (id_color>0):
            colores=list(Color.objects.filter(id_color=id_color).values())
            if len(colores) > 0:
                color=colores[0]
                datos={'message':"Success",'colores':color}
            else:
                datos={'message':"colores no encontrados..."}
            return JsonResponse(datos)
        else:
            colores=list(Color.objects.values())
            if len(colores)>0:
                datos={'message':"Success",'colores':colores}
            else:
                datos={'message':"color no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Color.objects.create(
            color=jd['color']      
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_color):
        jd=json.loads(request.body)
        colores = list(Color.objects.filter(id_color=id_color).values())
        if len(colores) > 0:
            color=Color.objects.get(id_color=id_color)
            color.color=jd['color']
            color.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"color not found"}
        return JsonResponse(datos)



    def delete(self,request, id_color):
        colores = list(Color.objects.filter(id_color=id_color).values())
        if len(colores) > 0:
            Color.objects.filter(id_color=id_color).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "color no encontrado"}
        return JsonResponse(datos)