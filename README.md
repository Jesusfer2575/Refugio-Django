# Refugio-Django
Proyecto de refugio de animales basado en Django 


sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

sudo -u postgres psql

CREATE DATABASE pet;

CREATE USER postgres WITH PASSWORD 'password';

ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE pet TO postgres;

\q


sudo pip install virtualenv

mkdir ~/pet
cd ~/pet

virtualenv env

source env/bin/activate

pip install django psycopg2

git clone https://github.com/Jesusfer2575/Refugio-Django.git

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


cd ~/pet
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

sudo ufw allow 8000

python manage.py runserver

http://localhost:8000
