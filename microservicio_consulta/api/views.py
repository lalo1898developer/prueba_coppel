import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Usuarios, Comics
from api.serializers import ComicsSerializer
from project.settings import SECRET_KEY

class ListView(APIView):
    def get(self, request):
        # Validamos que exista el usuario
        token = request.headers['Authorization']
        token_split = token.split(' ')
        decode = jwt.decode(token_split[1], SECRET_KEY, algorithms="HS256")
        
        if len(Usuarios.objects.filter(id=decode['id'])) == 1:
            if len(request.GET) != 0:
                orderby = request.GET['orderby']
                comics = Comics.objects.filter(user_id=decode['id']).order_by(orderby)
            else:
                comics = Comics.objects.filter(user_id=decode['id'])
            
            comics_serializer = ComicsSerializer(comics, many=True)
            return Response(comics_serializer.data)
