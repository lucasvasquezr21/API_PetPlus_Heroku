
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Animal

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class AnimalView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_animal=0):
        if (id_animal>0):
            animales=list(Animal.objects.filter(id_animal=id_animal).values())
            if len(animales) > 0:
                animal=animales[0]
                datos={'message':"Success",'animales':animal}
            else:
                datos={'message':"Animales no encontrados..."}
            return JsonResponse(datos)
        else:
            animales=list(Animal.objects.values())
            if len(animales)>0:
                datos={'message':"Success",'animales':animales}
            else:
                datos={'message':"Animales no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Animal.objects.create(
            nombre=jd['nombre'],
            n_microchip=jd['n_microchip'],
            tipo_sangre=jd['tipo_sangre'],
            dueno_id_dueno_id=jd['dueno_id_dueno_id'],
            color_id_color_id=jd['color_id_color_id'],
            especie_id_especie_id=jd['especie_id_especie_id'],
            estado_id_estado_id=jd['estado_id_estado_id'],
            sexo_id_sexo_id=jd['sexo_id_sexo_id'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_animal):
        jd=json.loads(request.body)
        animales = list(Animal.objects.filter(id_animal=id_animal).values())
        if len(animales) > 0:
            animal=Animal.objects.get(id_animal=id_animal)
            animal.nombre=jd['nombre']
            animal.n_microchip=jd['n_microchip']
            animal.dueno_id_dueno=jd['dueno_id_dueno']
            animal.color_id_color=jd['color_id_color_id']
            animal.especie_id_especie=jd['especie_id_especie']
            animal.estado_id_estado=jd['estado_id_estado']
            animal.sexo_id_sexo=jd['sexo_id_sexo']
            animal.tipo_sangre=jd['tipo_sangre']
            animal.save()
            datos = {'mesage':"Success"}
        else:
            datos = {'message':"Animal not found"}
        return JsonResponse(datos)

    def delete(self,request, id_animal):
        animales = list(Animal.objects.filter(id_animal=id_animal).values())
        if len(animales) > 0:
            Animal.objects.filter(id_animal=id_animal).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Animal no encontrado"}
        return JsonResponse(datos)