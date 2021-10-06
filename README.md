# API REST

## que hace:
Esta es un api rest para insercion actualizacion y obtencion de datos de la bd de koha.
este codigo no permite el borrado de datos por seguridad, es simplemente un puente de conexion de koha, con delphi.
la idea es que este disponible para envios y recepcion de datos por parte simultanea de las dos entidades.
cualquier duda se puede comunicar con delphy analitics

## prerequisitos:
credenciales de la base de datos de koha
python3
flask

## como instalarlo:

Para instalarlo primero debe configurar las credenciales de la base de datos en el archivo operationBD.py. Despues de la conexion establecida ya puede comenzar el despliegue, el api rest es realizado en el framework flask. 

### primero: 
modifique el archivo operationBd.py poniendo las credenciales de la base de datos de koha que se necesitan. NOTA: quedara comentado las linea a  modificar, espero no tegan problema, cualquier cosa puede informar a delphy para su solucion en conjunto.

### segundo: 
instalar ngxis

### tercero: 
generar el archivo de configuracion correspondiente en la carpeta /etc/nginx/sites-available

### cuarto:
generar el link virtual de sites available a sites enabled

### quinto
instalar gunicorn

### sexto 
configurar gunicorn

### septimo 
revisar los servcios de gunicorn y nginx



## info util: 
el api esta montado en flask, el archivo de requirimientos se encuentra como un txt recomendamos usar gunicorn con ngnx

puede tomar de aqui la configuracion basica de nginx y gunicorn:
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#check-for-the-gunicorn-socket-file 
