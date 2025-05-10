from flask import render_template, Blueprint, request, session, redirect, url_for, flash, g
from .query import *
from werkzeug.security import check_password_hash, generate_password_hash
import re

login_team = Blueprint('login_team', __name__)

@login_team.route('/login_team', methods=['POST', 'GET'])
def do_login_team():
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
            return redirect(url_for('login_team.session_employee', id_employee=result[0]))
        else:
            error = 'Usuario, contraseña o numero de telefono incorrectos' if lang == 'es' else 'Incorrect username, password or phone number'
            flash(error, 'error')
            return redirect(url_for('login_team.do_login_team'))

    return render_template('logins_sessions/login_team.html', data=data)

@login_team.route('/session/empleado/<int:id_employee>')
def session_employee(id_employee):
    return 'Exito empleado'