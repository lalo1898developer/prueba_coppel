from rest_framework import serializers
from api.models import Usuarios, Comics

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'name', 'age', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('id', 'title', 'image', 'onsaleDate', 'user_id')
