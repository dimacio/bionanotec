from flask import render_template
from app import app_obj
from .models import Paper
from .models import Team
from .models import News
from .models import Linea


@app_obj.route("/")
def home():
    return render_template("home.html",news=News.query.all())


@app_obj.route("/equipo/")
def equipo():
    return render_template("equipo.html",team=Team.query.all())


@app_obj.route("/investigación/")
def investigación():
    return render_template("investigación.html",lineas=Linea.query.all())
#aca son todas las lineas
@app_obj.route("/linea/<id>")
def linea(id):
    linea = Linea.query.get_or_404(id)
    return render_template("linea.html", linea=linea)

@app_obj.route("/publicaciones/")
def publicaciones():
    years = [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010]
    return render_template("publicaciones.html", papers=Paper.query.all(),years=years)
# hay que agregar como parametro la base de datos que queres usar


if __name__ == "__main__":
    app_obj.run(debug=True)


# if the the server is already used
# sudo lsof -i :5000  to detect the process listening on the port

# and then sudo kill -9 <process_id>
