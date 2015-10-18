import flask

from roomSelector import app
from roomSelector.models import User
from roomSelector.database import db_session


@app.route('/')
def home_page():
    user_id = flask.session.get('logged_in')
    user = None
    user_is_admin = None
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        user_is_admin = user.type.name == 'admin'
    return flask.render_template('gateway.html', user=user, user_is_admin=user_is_admin)

@app.route('/member')
def member_page():
    return flask.render_template('member.html')

@app.route('/manager')
def manager_page():
    return flask.render_template('manager.html')

@app.route('/rooms')
def room_page():
    return flask.render_template('rooms.html')

@app.route('/chores')
def chores_page():
    return flask.render_template('chores.html')

@app.route('/reimbursements')
def reimbursements_page():
    return flask.render_template('chores.html')





 
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