from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app_obj = Flask(__name__)
bootstrap = Bootstrap(app_obj)
app_obj.config.from_object(Config)
db = SQLAlchemy(app_obj)
migrate = Migrate(app_obj, db)


from app import routes, models
# do not pay attention to the alert of lintern or you will fall in to a circular
# calling that it's a nightmare
