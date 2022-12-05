import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_usuario=0):
        if (id_usuario>0):
            usuarios=list(Usuario.objects.filter(id_usuario=id_usuario).values())
            if len(usuarios) > 0:
                usuario=usuarios[0]
                datos={'usuarios':usuario}
            else:
                datos={"usuarios no encontrados..."}
            return JsonResponse(datos)
        else:
            usuarios=list(Usuario.objects.values())
            if len(usuarios)>0:
                datos={'message':"Success",'usuarios':usuarios}
            else:
                datos={'message':"usuarios no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Usuario.objects.create(
            usuario=jd['usuario'],
            contrasena=jd['contrasena'],
            emp_id_emp_id=jd['emp_id_emp_id'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_usuario):
        jd=json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id_usuario=id_usuario).values())
        if len(usuarios) > 0:
            usuario=Usuario.objects.get(id_usuario=id_usuario)
            usuario.usuario=jd['usuario']
            usuario.contrasena=jd['contrasena']
            usuario.emp_id_emp=jd['emp_id_emp']
            usuario.save()
            datos = {'mesage':"Success"}
        else:
            datos = {'message':"usuario not found"}
        return JsonResponse(datos)

    def delete(self,request, id_usuario):
        usuarios = list(Usuario.objects.filter(id_usuario=id_usuario).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id_usuario=id_usuario).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "usuario no encontrado"}
        return JsonResponse(datos)