from app import app_obj, db
from app.models import Paper, Team, News, Linea


@app_obj.shell_context_processor
def make_shell_context():
    return {'db': db, 'Paper': Paper, "Team" : Team, "News" : News , "Linea" : Linea}

