# Proyecto Urban Grocers 

El proyecto se trata de llevar a cabo una serie de pruebas automatizadas mediante una lista de comprobación para el campo “name” en la solicitud de creación de un kit de productos.

Para ello necesitamos trabajar con tres archivos donde obtendremos nuestras solicitudes a la hora de automatizar las pruebas:

Para llevar a cabo la tarea trabaje con estos tres archivos: 

•	configuration.py
•	data.py
•	sender_stand_request.py

a) el archivo “configuration.py” contiene lo siguiente:

La URL de la API y los endpoits. 

•	URL_SERVICE = "https://cnt-a9dbc58d-f802-4f46-bb35-8b64ec080f7e.containerhub.tripleten-services.com"
•	CREATE_USER_PATH = "/api/v1/users”
•	KITS_PATH = "/api/v1/kits"

b) el archivo “data.py” contiene lo siguiente:

En este archivo colocamos los encabezados y los cuerpos de las solicitudes en formato Json.

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {'authToken'}"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

kit_body = {
       "name": "Mi conjunto",
}

En el archivo create_kit_name_kit_test.py es donde se llevara a cabo nuestras pruebas automatizadas de la lista de comprobación, con la ayuda de los archivos anteriormente mencionados.

Aquí se configuraron las funciones y nuestros parámetros para llevar a cabo nuestras pruebas positivas y negativas. Y la definición de funciones para cada caso de prueba.

Verifica tener instalado Pytest, actualizar la URL y tener el authToken en la autorización para poder correr las pruebas.
