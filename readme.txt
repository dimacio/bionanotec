activar el entorno:

$source bionanotec_env/bin/activate

----------Actualización de la pagina----------------
Para agregar nuevas actualizaciones correr desde la carpeta bionanotec

$git init

$git add .

$git commit -m "nota de referencia"

$heroku git:remote --app bionantec

$git push heroku master

-----------------------------------------------------



-----app/routes.py-----
Gestiona el render de los html, cada seccion que hagas tenes que agregar una ruta aca que
te mande al template que queres

-----app/models.py-----
Define la estructura de la base de datos por un modelo relacional, cada columna es un 
parametro que vamos a pode recuperar. Usando la extension excel viewer se puede editar
desde el visual studio code


para cambiar los papers hay que borrar la carpeta migrate y app.db despues correr 

no carga imagenes en png  y tienen que estaR en kla carpeta static

flask db init
flask db migrate -m "nota"
flask db upgrade

para crear la base de datos
despues correr el programa csv_db.py y volver a correr todo lo anterior para actualizAR LA BASE DE DATOS

HAY QUE FIJARSE QUE LOS STRING DEL CSV ESTEN ENTRE COMILLAS O NO SE CARGAN


-----papers_frontend.py-----

permite una GUI para administrar la base de datos de papers
la gracia seria hacer una para cada clase de contenidos 
evitando la interacción directa con el codigo de la pagina