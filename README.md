# ecommerces

Project Ecommerce
----------------------------------------------------------------------------------------------------
El proyecto está desarrollado con el lenguaje de programación Python, se debe instalar Python v3.6.7. Con los siguientes comandos puede instalar Python y PIP.

Entrar como root o super usaurio para la instalacion

$ aptitude install python3.6 python3-pip python3.6-dev python3-setuptools

$ aptitude install python3-virtualenv virtualenvwrapper

Salir del modo root y crear el ambiente:

$ mkvirtualenv --python=/usr/bin/python3 ecommerce
----------------------------------------------------------------------------------------------------
Para descargar el código fuente del proyecto contenido en su repositorio GIT realice un clon del proyecto:

$ git clone https://github.com/carlosnp/ecommerces.git
----------------------------------------------------------------------------------------------------
Para instalar los requirimientos del proyecto con el siguiente comando:

$ pip install -r requirements.txt
----------------------------------------------------------------------------------------------------
Para cargar los datos iniciales y cuenta de usuarios del sistema y administrador de la plataforma de ingresar el siguiente comando:

$ python manage.py loaddata fixtures/initial_data_product_name.json