import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import TipoEmp

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class TipoEmpView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_tipo_emp=0):
        if (id_tipo_emp>0):
            tipoemps=list(TipoEmp.objects.filter(id_tipo_emp=id_tipo_emp).values())
            if len(tipoemps) > 0:
                tipoemp=tipoemps[0]
                datos={'message':"Success",'tipoemps':tipoemp}
            else:
                datos={'message':"tipoemps no encontrados..."}
            return JsonResponse(datos)
        else:
            tipoemps=list(TipoEmp.objects.values())
            if len(tipoemps)>0:
                datos={'message':"Success",'tipoemps':tipoemps}
            else:
                datos={'message':"tipoemp no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        TipoEmp.objects.create(
            nombre_tipo_emp=jd['nombre_tipo_emp']
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_tipo_emp):
        jd=json.loads(request.body)
        tipoemps = list(TipoEmp.objects.filter(id_tipo_emp=id_tipo_emp).values())
        if len(tipoemps) > 0:
            tipoemp=TipoEmp.objects.get(id_tipo_emp=id_tipo_emp)
            tipoemp.nombre_tipo_emp=jd['nombre_tipo_emp']
            tipoemp.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"tipoemp not found"}
        return JsonResponse(datos)



    def delete(self,request, id_tipo_emp):
        tipoemps = list(TipoEmp.objects.filter(id_tipo_emp=id_tipo_emp).values())
        if len(tipoemps) > 0:
            TipoEmp.objects.filter(id_tipo_emp=id_tipo_emp).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "tipoemp no encontrado"}
        return JsonResponse(datos)