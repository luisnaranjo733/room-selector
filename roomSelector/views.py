import flask

from roomSelector import app
from roomSelector.models import User
from roomSelector.database import db_session

import state



@app.route('/')
def home_page():
    params = {
        'user_id': flask.session.get('logged_in'),
        'user': None,
        'user_is_admin': None,
        'selectionOn': state.selectionStatus(),
        'people': User.query.filter (User.is_live_in == True).order_by(User.house_points.desc()),
    }
    if params['user_id']:
        user = User.query.filter(User.id == params['user_id']).first()
        is_admin = user.type.name == 'admin'
        if is_admin:
            template = 'manager.html'
        else:
            template = 'member.html'
        return flask.render_template(template, **params)
    return flask.render_template('cover.html')

@app.route('/endit')
def endit():
    print 'endit'
    state.stopSelection()
    return flask.redirect(flask.url_for('home_page'))

@app.route('/startit')
def startit():
    print 'startit'
    state.startSelection()
    return flask.redirect(flask.url_for('home_page'))

@app.route('/rooms')
def room_page():
    params = {
        'people': User.query.filter (User.is_live_in == True).order_by(User.house_points.desc()),
    }
    return flask.render_template('rooms.html', **params)

@app.route('/chores')
def chores_page():
    params = {
        'people': User.query.filter (User.is_live_in == True).order_by(User.house_points.desc()),
    }
    return flask.render_template('chores.html', **params)

@app.route('/reimbursements')
def reimbursements_page():
    params = {
        'people': User.query.filter (User.is_live_in == True).order_by(User.house_points.desc()),
    }
    return flask.render_template('reimbursements.html', **params)


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
                return flask.redirect(flask.url_for('home_page'))
                
        flask.flash('Invalid username/password')  # this will only happen if auth failed

    return flask.render_template('signin.html', **params)
    
@app.route('/logout')
def logout():
    flask.session['logged_in'] = ''
    return flask.redirect(flask.url_for('home_page'))