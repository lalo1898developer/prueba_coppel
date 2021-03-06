# Prueba de Coppel

En el archivo "requerimientos.pdf", contiene la descripción a detalle de cada caso de uso a realizar.
En resumen se compone de 4 microservicios:

1. Microservicio de Busqueda: consultara a una API externa comics o personajes segun sea el caso.
2. Microservicio de Usuarios: servira para registrar y autenticar con usuario y contraseña. (retorna un jwt)
3. Microservicio de Ingesta: solo los usuarios registrados podran agregar a su lista la cantidad de comics que deseen solo mandando el o los 'id' de estos.
4. Microservicio de Consulta: solo los usuarios registrados podran consultar sus comics guardados.

## Instalación

### Requisitos previos

- docker
- docker-compose
- descargar o copiar contenido del archivo 'docker-compose.yml' de este directorio.

Realizar el siguiente comando en la consola de su preferencia, en la direccion donde tenga el archivo docker-compose almacenado.

```bash
docker-compose build
docker-compose up #puedes colocar la bandera '-d' si quieres que no se quede tu consola con los servicios
```

## Como usar

Importe el archivo *thunder-collection_PruebaCoppel.json* a su cliente 'Thunder Client' para consultar y poder probar las funcionalidades de los microservicios.

## Propietario
Eduardo Rodriguez Ricardez

## License
None
