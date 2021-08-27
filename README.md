# API REST

## funcion:
para insercion actualizacion y obtencion de datos de la bd de koha. Para instalarlo primero debe configurar las credenciales de la base de datos en el archivo operationBD.py. Despues de la conexion establecida ya puede comenzar el despliegue, el api rest es realizado en el framework flask. cualquier duda se puede comunicar con delphy analitics

## como instalarlo:
### primero: 
modifique el archivo operationBd.py poniendo las credenciales de la base de datos de koha que se necesitan. NOTA: quedara comentado las linea a  modificar, espero no tega problemam, cualquier cosa puede informar a delphy para su solucion en conjunto.
### segundo: 
el api esta montado en flask, el archivo de requirimientos se encuentra como un txt recomendamos usar gunicorn con ngnx