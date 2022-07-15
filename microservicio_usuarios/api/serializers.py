from rest_framework import serializers
from api.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'name', 'age', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }