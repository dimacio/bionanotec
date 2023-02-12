activar el entorno:

$source bionanotec_env/bin/activate

----------Actualización de la pagina cuando era gratis heroku----------------
Para agregar nuevas actualizaciones correr desde la carpeta bionanotec

$git init

$git add .

$git commit -m "nota de referencia"

$heroku git:remote --app bionantec

$git push heroku master

----------------------para correr en render-------------------------------

Render no lee el procfile para ver como tiene que armar la pagina así que para darle el comando correcto de gunicorn 
tenes que ir a la parte de setting en el dashboard y definir ahí el comando de inicio (start Command)

Start Command

This command runs in the root directory of your app and is responsible for starting its processes. It is typically used to start a webserver for your app. It can access environment variables defined by you in Render.

poniendo "gunicorn start_here:app_obj" logre hacer un "Deploy live" sin errores pero igual la página esta caida, no se si es porque es servicio gratuito no soporta mi página


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
