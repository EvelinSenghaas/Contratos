Para Ejecutar el proyecto

1. Crear un entorno virtual con virtualenv
2. Una vez activado el entorno dirigirse a la carpeta project
3. instalar la dependencias pip install -r requirements.txt 
4. configurar tu archivo .env *(podes borrar .example y cargar tus datos ahi)
5. ejecutar python manage.py makemigrations
6. ejecutar python manage.py migrate
7. ejecutar python manage.py createsuperuser *(cuando accedas a la url te va a pedir loggearte, ingresa los mismos datos que cargues aca)
8. ejecutar python manage.py runserver
9. Ya esta! podes ir a la url: localhost:8000/Home
