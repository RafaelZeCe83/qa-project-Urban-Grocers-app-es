# Proyecto Urban Grocers - Rafael Zermeño Cervantes – Srpint 7 – QA14

Para llevar a cabo los casos de prueba para el proyecto: “create_kit_name_kit_test.py”

Es necesario instalar los siguientes programas:

A. intérprete de Python  https://www.python.org/downloads/
Entrar a la página oficial en descargas y dar clic al botón amarillo (detecta automáticamente tu sistema operativo). Descargar e instalar.
Una vez instalado es necesario hacer unas configuraciones en Windows para evitar conflictos con Python y el resto de los programas que necesitaremos:
1.- Ubicar el archivo de instalación del intérprete de Python y obtener la ruta. En mi caso es:
C:\Users\Spartan83\AppData\Local\Programs\Python\Python312
De igual manera ubicar las siguientes carpetas: Scripts y site-packages y obtener las rutas:
C:\Users\Spartan83\AppData\Local\Programs\Python\Python312\Scripts
C:\Users\Spartan83\AppData\Local\Programs\Python\Python312\Lib\site-packages
2.- ir a configuración avanzada del sistema > Opciones avanzadas > variables de entorno
-	En variables de usuario seleccionar "Path" y dar clic en Editar. 
-	Dar clic en "nuevo" y añadir uno a uno las rutas.
NOTA: Posicionar las 3 rutas en las primeras 3 posiciones con el botón subir, para evitar conflictos con otros programas. Todo esto es con la finalidad de poder instalar las librerías, pytest, pip, etc. para llevar a cabo las instalaciones necesarias en los programas que ocuparemos en nuestro proyecto.
________________________________________________________________________________
B. Otro programa que necesitaremos instalar es: PyCharm
Pycharm es un programa para escribir código y tiene una herramienta de edición de código que resalta los errores, los corrige y automatiza la rutina de programación.
Una vez instalado, instala las librerías de la siguiente manera:
En la parte inferior se encuentra la consola de Python. Hay dos formas de instalar. La más fácil es ir a icono que “Python packages” y en la barra de búsqueda teclear:
-	Pip y elegir la última versión e instalar.
-	Pytest, y elegir la última versión e instalar.
-	Request e instalar (esta es nuestra librería) 
Otra manera es teclear en la terminal:
•	pip install pytest
•	pip install requests
_________________________________________________________________________________
C. Otro programa que necesitaremos instalar es: Git:
Git es un sistema de control de versiones distribuido que sirve para gestionar y rastrear cambios en archivos y proyectos, especialmente en el desarrollo de software. Mejorando la organización, la colaboración y la gestión del código.

_________________________________________________________________________________
OBJETIVO DEL PROYECTO:

El proyecto se trata de llevar a cabo una serie de pruebas automatizadas mediante una lista de comprobación para el campo “name” en la solicitud de creación de un kit de productos
Para ello necesitamos trabajar con tres archivos donde obtendremos nuestras solicitudes a la hora de automatizar las pruebas:
Para llevar a cabo la tarea trabaje con estos tres archivos: 

•	configuration.py – Este archivo generalmente se utiliza para almacenar configuraciones del proyecto, como parámetros, constantes o ajustes que se pueden modificar sin cambiar el código principal. Puede incluir configuraciones de bases de datos, claves de API, rutas de archivos, etc. Aquí colocaremos las URL de la API y el token de la autenticación.
•	data.py – Este archivo suele estar destinado a la gestión y manipulación de datos. Puede incluir funciones para cargar, procesar y guardar datos, así como definir estructuras de datos o modelos. En este caso tendremos los cuerpos de las solicitudes en formato json y las variables que emplearemos en nuestro proyecto.
•	sender_stand_request.py - Este archivo suele estar destinado a la gestión y manipulación de datos. Puede incluir funciones para cargar, procesar y guardar datos, así como definir estructuras de datos o modelos. En nuestro caso aquí estarán nuestras solicitudes POST de la API para creación de usuario y un nuevo kit.


En el archivo create_kit_name_kit_test.py es donde se llevara a cabo nuestras pruebas automatizadas de la lista de comprobación, con la ayuda de los archivos anteriormente mencionados.

Aquí se configuraron las funciones y nuestros parámetros para llevar a cabo nuestras pruebas positivas y negativas. Y la definición de funciones para cada caso de prueba.

Verifica tener instalado Pytest, actualizar la URL y tener el authToken en la autorización para poder correr las pruebas, como vimos al principio, de lo contrario no podremos arrancar las pruebas.

Para ejecutar las pruebas hay que hacer lo siguiente. Hay que configurar la ejecución de la prueba:
•	Ir a Run > Edit Configurations.
•	Haz clic en el botón "+" y selecciona "Python tests" y luego "pytest".
•	Configura el nombre y el directorio o archivo de prueba que deseas ejecutar, y haz clic en "OK".


Ahora ponemos ejecutar esta configuración desde el menú desplegable en la esquina superior derecha.

Otra manera es desde la terminal escribiendo:

Pytest y enseguida el nombre de nuestro archivo

Ej:

pytest create_kit_name_kit_test.py






