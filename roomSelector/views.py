import flask

from roomSelector import app
from roomSelector.models import User
from roomSelector.database import db_session


@app.route('/')
def home():
    users = User.query.all()
    return flask.render_template('home.html', users=users)
 