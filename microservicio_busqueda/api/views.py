import requests

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.serializers import serializePersonajes, serializeComics
from project.settings import MARVEL_API_PUBLICKEY, MARVEL_HASH

@csrf_exempt
def busquedaApi(request):
    if request.method=='GET':
        base_req_url = 'https://gateway.marvel.com/v1/public/'
        
        base_req_parms = {
            'apikey': MARVEL_API_PUBLICKEY,
            'ts': '1',
            'hash': MARVEL_HASH,
            'limit': '99'
        }
        
        try:
            if len(request.GET) != 0:
                tipo_param = request.GET['tipo']
            
                if tipo_param == 'comics':
                    # Busqueda por comics
                    personaje_o_comic = 'comics'
                    base_req_parms['orderBy'] = 'title'
                elif tipo_param == 'personajes':
                    # Busqueda por personajes
                    personaje_o_comic = 'characters'
                    base_req_parms['orderBy'] = 'name'
                    
            else:
                # Busqueda default
                tipo_param = 'personajes'
                personaje_o_comic = 'characters'
                base_req_parms['orderBy'] = 'name'
                
            if len(request.GET) == 2:
                filtro = '/' + request.GET['filtro']
            else:
                filtro = ''
                
            r = requests.get(
                base_req_url + personaje_o_comic + filtro,
                params = base_req_parms,
            )
            
            if r.status_code != 200:
                print("Ocurrio un error en la peticion http")
            else:
                data = r.json()['data']['results']
                
                if tipo_param == 'comics':
                    comics_serializer = serializeComics(data)
                    return JsonResponse(comics_serializer, safe=False)
                elif tipo_param == 'personajes':
                    personajes_serializer = serializePersonajes(data)
                    return JsonResponse(personajes_serializer, safe=False)
                
        except:
            print("Ocurrio una excepcion")

# Create your views here.
