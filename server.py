import requests
import os
from sessions import RedisSessionInterface
from datetime import timedelta, datetime, date
from flask import (Flask, render_template, g, redirect, url_for, request,
                   session, abort)


app = Flask(__name__)
app_root = os.path.dirname(os.path.abspath(__file__))
app.session_interface = RedisSessionInterface()
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

@app.before_request
def b4req():
    g.user = None
    if('user' in session):
        g.user = session['user']

@app.route('/')
def index():
    if(not g.user):
        return redirect(url_for('login'))

    return render_template('index.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if(g.user):
        return abort(404)

    if(request.method == 'POST'):
        session.pop('user', None)
        req = request.form
        if(True):
            session.permanent = True
            session['user'] = req['username']
            return redirect(url_for('index'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    if(not g.user):
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/busca')
def busca():
    if(not g.user):
        return redirect(url_for('login'))

    return render_template('busca.html')


@app.route('/sair')
def sair():
    session.pop('user', None)
    return redirect(url_for('index'))