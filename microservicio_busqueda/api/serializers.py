from api.models import Personajes, Comics

def serializePersonajes(personajes):
    personajes_serializados = []
    
    for personaje in personajes:
        p = Personajes(
            personaje['id'], 
            personaje['name'], 
            personaje['thumbnail']['path'], 
            personaje['comics']['available']
        )
        
        personajes_serializados.append(p.__dict__)
    
    return personajes_serializados

def serializeComics(comics):
    comics_serializados = []
    
    for comic in comics:
        onsaleDate = [date for date in comic['dates'] if date['type'] == 'onsaleDate']
        
        c = Comics(
            comic['id'], 
            comic['title'], 
            comic['thumbnail']['path'], 
            onsaleDate[0]['date']
        )
        
        comics_serializados.append(c.__dict__)
    
    return comics_serializados
