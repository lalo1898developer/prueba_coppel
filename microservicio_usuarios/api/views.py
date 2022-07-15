import jwt
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from api.models import Usuarios
from api.serializers import UsuariosSerializer
from project.settings import SECRET_KEY
from django.contrib.auth.hashers import make_password, check_password

class CreateView(APIView):
    def post(self, request):
        if len(request.data) == 3:
            # Creamos un usuario nuevo
            encryptedpassword=make_password(request.data['password'])
            request.data['password'] = encryptedpassword
            usuarios_serializer = UsuariosSerializer(data = request.data)
        
            if usuarios_serializer.is_valid():
                usuarios_serializer.save()
                return Response('Usuario agregado existosamente')
            else:
                raise ValidationError('Hubo un error al agregar al usuario')
        else:
            # Logeamos un usuario
            name = request.data['name']
            password = request.data['password']
            usuario_data = Usuarios.objects.filter(name=name).first()
            
            if usuario_data is None:
                raise AuthenticationFailed('Usuario no encontrado')
            
            if not check_password(password, usuario_data.password):
                raise AuthenticationFailed('Contraseña incorrecta')
            
            payload = {
                'id': usuario_data.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            
            usuario_serializer = UsuariosSerializer(usuario_data)
            usuario_serializer.data['token'] = token
            
            response = Response()
            response.data = usuario_serializer.data
            response.data['token'] = token
            
            return response
