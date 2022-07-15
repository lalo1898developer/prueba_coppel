import jwt
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Usuarios
from api.serializers import ComicsSerializer
from project.settings import SECRET_KEY

class AddView(APIView):
    def post(self, request):
        # Validamos que exista el usuario
        token = request.headers['Authorization']
        token_split = token.split(' ')
        decode = jwt.decode(token_split[1], SECRET_KEY, algorithms="HS256")
        if len(Usuarios.objects.filter(id=decode['id'])) == 1:
            # Validamos el id o ids de los comics o personajes enviados
            base_req_url = 'http://mcsbusqueda:8000/searchComics'
            
            for element in request.data:
                base_req_parms = {
                    'tipo': 'comics',
                    'filtro': element['id']
                }
                
                r = requests.get(
                    base_req_url,
                    params = base_req_parms,
                )
                
                if r.status_code != 200:
                    print("Ocurrio un error en la peticion http")
                else:
                    # Agregamos el comic
                    data = r.json()
                    data[0]['user_id'] = decode['id']
                    comics_serializer = ComicsSerializer(data=data[0])
                    comics_serializer.is_valid(raise_exception=True)
                    comics_serializer.save()

            return Response('Comics agregados correctamente')
