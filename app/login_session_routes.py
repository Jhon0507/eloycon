from flask import render_template, Blueprint, request, session, redirect, url_for, flash
from .query import *
from werkzeug.security import check_password_hash, generate_password_hash
import re

logins = Blueprint('login', __name__)

@logins.route('/login_client', methods=['POST', 'GET'])
def login_client():
    lang = session.get('lang', 'es')
    data = ['Cliente Login', 'usuario', 'contraseña', 'Entrar', 'Registrarse'] if lang == 'es' \
        else ['Client Login', 'username', 'password', 'Login', 'Register']

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = get_user_password_client(username)  # get id and password from the possible username

        if result and check_password_hash(result[1], password):
            return redirect(url_for('login.session_client', id_client=result[0]))
        else:
            error = 'Usuario o contraseña incorrecto' if lang == 'es' else 'Incorrect username or password'
            flash(error, 'error')
            return redirect(url_for('login.login_client'))

    return render_template('logins_sessions/login_client.html', data=data)


@logins.route('/login_team', methods=['POST', 'GET'])
def login_team():
    lang = session.get('lang', 'es')
    data = ['Equipo Login', 'usuario', 'contraseña','numero de telefono', 'Entrar'] if lang == 'es' \
        else ['Team Login', 'username', 'password', 'phone number', 'Login']

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']

        result = get_user_password_employee(username)  # get id, phone and password from the possible username
        transform_number = re.sub(r'^\+\d+\s*', '', result[1]).replace(' ', '')  # +34 123 456 789 --> 123456789

        if result and transform_number == phone and check_password_hash(result[2], password):
            return redirect(url_for('login.session_employee', id_employee=result[0]))
        else:
            error = 'Usuario, contraseña o numero de telefono incorrectos' if lang == 'es' else 'Incorrect username, password or phone number'
            flash(error, 'error')
            return redirect(url_for('login.login_team'))

    return render_template('logins_sessions/login_team.html', data=data)


@logins.route('/session/cliente/<int:id_client>')
def session_client(id_client):
    return 'Exito'


@logins.route('/session/empleado/<int:id_employee>')
def session_employee(id_employee):
    return 'Exito empleado'