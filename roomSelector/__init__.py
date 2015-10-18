from flask import Flask

app = Flask(__name__)
app.secret_key = 'Drake1848'

# Import the view module after the application object is created.
import roomSelector.views
from roomSelector.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



