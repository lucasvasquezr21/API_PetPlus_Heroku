import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Emp

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class EmpView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get(self,request,id_emp=0):
        if (id_emp>0):
            emps=list(Emp.objects.filter(id_emp=id_emp).values())
            if len(emps) > 0:
                emp=emps[0]
                datos={'message':"Success",'empleados':emp}
            else:
                datos={'message':"empleados no encontrados..."}
            return JsonResponse(datos)
        else:
            emps=list(Emp.objects.values())
            if len(emps)>0:
                datos={'message':"Success",'emps':emps}
            else:
                datos={'message':"Empleados no encontrados..."}
            return JsonResponse(datos)


    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Emp.objects.create(
            nombre_empleado=jd['nombre_empleado'],
            tipo_empleado_id_tipo_empleado_id=jd['tipo_empleado_id_tipo_empleado_id'],     
            veterinaria_id_veterinaria_id=jd['veterinaria_id_veterinaria_id'],
            tipo_emp=jd['tipo_emp'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)


    def put(self,request,id_emp):
        jd=json.loads(request.body)
        emps = list(Emp.objects.filter(id_emp=id_emp).values())
        if len(emps) > 0:
            emp=Emp.objects.get(id_emp=id_emp)
            emp.nombre_empleado=jd['nombre_empleado']
            emp.tipo_emp=jd['tipo_emp']
            emp.veterinaria_id_veterinaria=jd['veterinaria_id_veterinaria']
            emp.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"emp not found"}
        return JsonResponse(datos)


    def delete(self,request, id_emp):
        emps = list(Emp.objects.filter(id_emp=id_emp).values())
        if len(emps) > 0:
            Emp.objects.filter(id_emp=id_emp).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "emp no encontrado"}
        return JsonResponse(datos)