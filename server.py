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


@app.route('/')
def index():

    return render_template('busca.html')



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
            return redirect(url_for('cadastro'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/cadastro')
def pontos_cadastro():
    if(not g.user):
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/busca')
def pontos_cadastro():
    if(not g.user):
        return redirect(url_for('login'))

    return render_template('cadastro.html')