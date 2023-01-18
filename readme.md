# Proyecto Portal Campana

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona el proyecto
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```

## Notas e instrucciones de la plataforma
+ En la página inicial se puede observar un mensaje de bienvenida y el menú superior de navegación.
+ Para consultar la lista de las diferentes categorías hacer click en una de ellas.
+ Dentro de cada categoría se podrá ver la lista disponible, el cuadro de búsqueda y un botón para agregar contenido.
+ Para buscar en la lista simplemente se debe escribir en el cuadro de búsqueda y presionar el botón "buscar".
+ En la sección de agregar contenido se deben llenar los campos y presionar el botón "agregar"
+ Sección "Comercios" - La busqueda podrá ser por Nombre o Categoría del comercio.
+ Sección "Gastronomía" - La busqueda podrá ser por Nombre o Especialidad del comercio.
+ Sección "Propiedades" - La busqueda podrá ser por Tipo de propiedad u operación.
+ Sección "Clasificados" - La busqueda podrá ser por Producto o Descripción.

## Términos y condiciones
+ Proyecto creado por Eugenio Garcia para la academia Coderhouse durante el curso de Phyton.
+ Todo el contenido del proyecto es de propia autoría por lo que no se deben dar créditos correspondientes.
+ El proyecto fue creado exclusivamente con fines educativos. No utilizar con carácter comercial.