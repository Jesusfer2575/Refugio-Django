# Refugio-Django
Proyecto de refugio de animales basado en Django 

1) Actualizamos los paquetes localos, instalamos los paquetes necesarios
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

2) Accedemos al SG de postgreSQL desde una terminal en Ubuntu
sudo -u postgres psql

3) Creamos nuestra BD llamada 'pet'
CREATE DATABASE pet;

4) Creamos un usuario llamado 'postgres'
CREATE USER postgres WITH PASSWORD 'password';

5) Cambiamos algunas configuraciones para el usuario recien creado
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';

6) Le asignamos los permisos necesarios
GRANT ALL PRIVILEGES ON DATABASE pet TO postgres;

7) Salimos del gestor de bd
\q

8) Instalamos con el gestor de dependencias pip el programa virtualenv
sudo pip install virtualenv

9) Añadimos una carpeta para nuestro proyecto y accedemos a ella
mkdir ~/pet
cd ~/pet

10) Creamos un nuevo entorno virtual llamado 'env'
virtualenv env

11) Una vez creado, procedemos a activarlo con el siguiente comando, una vez activado nuestro prompt deberá haber cambiado
    con el prefijo del nombre del entorno virtual en este caso 'env'
source env/bin/activate

12) En este punto nos encontramos dentro de un entorno virtual, así que instalaremos el conector de BD con PostgreSQL
pip install django psycopg2

13) Clonamos el repositorio de GitHub
git clone https://github.com/Jesusfer2575/Refugio-Django.git

14) Una vez clonado iremos a la carpeta del proyecto, dentro habrá un archivo: '/Pruebas/settings.py', el cual contendrá el       Diccionario de Python DATABASES (vacío, ustedes tendrán que añadir el siguiente contenido)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pet',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

15) Retrocedemos una carpeta hasta estar en la raíz donde se encuentra el archivo manage.py del proyecto
cd ..
python manage.py makemigrations
python manage.py migrate

16) Creamos un superusuario para el administrador del proyecto 
python manage.py createsuperuser

17) Habilitamos el firewall del puerto 8000 mediante el comando ufw
sudo ufw allow 8000

18) Corremos el proyecto con
python manage.py runserver

19)Por último validamos que este corriendo localmente en cualquiera navegador
http://localhost:8000
