import flask

from roomSelector import app
from roomSelector.models import User
from roomSelector.database import db_session


@app.route('/')
def home():
    user_id = flask.session.get('logged_in')
    user = None
    if user_id:
        user = User.query.filter(User.id == user_id).first()
    return flask.render_template('home.html', user=user)

 
@app.route('/login', methods=['POST', 'GET'])
def login():
    params = {}
    if flask.request.method == 'POST':
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')
        
        params['email'] = email or ''
        
        user = User.query.filter(User.email == email).first()
        if user: # if email exists in database
            if user.checkPassword(password):
                flask.flash("Succesful authentication")
                flask.session['logged_in'] = user.id
                return flask.redirect(flask.url_for('home'))
                
        flask.flash('Invalid username/password')  # this will only happen if auth failed

    return flask.render_template('login.html', **params)
    
@app.route('/logout')
def logout():
    flask.session['logged_in'] = ''
    return flask.redirect(flask.url_for('home'))