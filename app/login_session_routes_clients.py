from flask import render_template, Blueprint, request, session, redirect, url_for, flash, g
from .query import *
from datetime import datetime
from decimal import Decimal
from werkzeug.security import check_password_hash, generate_password_hash
import re

login_client = Blueprint('login_client', __name__)

@login_client.before_request
def define_global_variables():
    lang_from_url = request.args.get('lang')
    if lang_from_url in ['es', 'en']:
        session['lang'] = lang_from_url

    language = session.get('lang', 'es')
    g.language = language
    g.title_historial = 'Historial de proyectos' if language == 'es' else 'Record projects'
    g.status = ['En revision', 'En desarrollo', 'Terminado', 'Cancelado'] if language == 'es' else ['Under review', 'On development', 'Finished', 'Canceled']
    g.no_projects = 'No tienes ningun proyecto registrado' if language == 'es' else "You don't have any registered project"
    g.no_img_project = 'Todavia no hay imagenes registradas de este proyecto' if language == 'es' else 'There are no images registered for this project yet.'
    g.data_project = ['Provincia', 'Fecha inicio', 'Fecha final', 'Presupuesto', 'Añadir proyecto'] if language == 'es' else ['Province', 'Start date', 'End date', 'Budget', 'Add project']
    g.submenu = ['actualizar datos', 'ver datos', 'cerrar sesión'] if language == 'es' else ['update data', 'view data', 'logout']

@login_client.context_processor
def inherit_global_client_variables():
    return dict(
        lang=g.get('language', 'es'),
        title_historial = g.get('title_historial', ''),
        status = g.get('status', []),
        no_projects = g.get('no_projects', ''),
        no_img_project = g.get('no_img_project', ''),
        data_project = g.get('data_project', []),
        submenu = g.get('submenu', '')
    )

@login_client.route('/login_client', methods=['POST', 'GET'])
def do_login_client():
    lang = session.get('lang', 'es')
    data = ['Cliente Login', 'usuario', 'contraseña', 'Entrar', 'Registrarse'] if lang == 'es' \
        else ['Client Login', 'username', 'password', 'Login', 'Register']

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = get_user_password_client(username)  # get id and password from the possible username

        if result and check_password_hash(result[1], password):
            return redirect(url_for('login_client.session_client', id_client=result[0]))
        else:
            error = 'Usuario o contraseña incorrecto' if lang == 'es' else 'Incorrect username or password'
            flash(error, 'error')
            return redirect(url_for('login_client.do_login_client'))

    return render_template('logins_sessions/login_client.html', data=data)

@login_client.route('/login_client/register', methods=['POST', 'GET'])
def register_new_client():
    lang = g.language
    title_register = 'Registrar nuevo cliente' if lang == 'es' else 'Register new client'
    data = ['Nombre', 'Apellidos', 'Email', 'Direccion', 'Telefono', 'Provincia', 'Usuario', 'Contraseña', 'Repetir Contraseña'] if lang == 'es' \
        else ['Name', 'Surnames', 'Email', 'Direction', 'Phone', 'Province', 'Username', 'Password', 'Repeat password']
    send = 'Registrarse' if lang == 'es' else 'Register'

    if request.method == 'POST':
        all_usernames = get_all_username_clients()
        all_emails = get_all_email_clients()
        if request.form['username'] in all_usernames:
            error = 'El nombre de usuario ya existe' if lang == 'es' else 'The username already exists'
            flash(error, 'error')
            return redirect(url_for('login_client.register_new_client'))
        elif request.form['email'] in all_emails:
            error = 'El correo ya esta registrado' if lang == 'es' else 'The email is already registered'
            flash(error, 'error')
            return redirect(url_for('login_client.register_new_client'))
        else:
            name = request.form['name']
            surnames = request.form['surnames']
            email = request.form['email']
            phone = request.form['phone']
            direction = request.form['direction']
            province = request.form['province']
            username = request.form['username']
            password = generate_password_hash(request.form['password'])
            insert_new_client(name, surnames, email, direction, phone, province, username, password)
            id_new_client = get_id_new_client(username)
            return redirect(url_for('login_client.session_client', id_client=id_new_client))

    return render_template('logins_sessions/register_client.html', title_register=title_register,
                           data=data, send=send)

@login_client.route('/session/cliente/<int:id_client>')
def session_client(id_client):
    lang = g.language
    data = get_info_client(id_client)
    historial = get_projects_client(id_client, lang)
    return render_template('logins_sessions/session_client.html', data=data, historial=historial)


@login_client.route('/session/cliente/<int:id_client>/add_project', methods=['POST', 'GET'])
def add_project_client(id_client):
    lang = g.language
    data = get_info_client(id_client)
    historial = get_projects_client(id_client, lang)
    send = 'Enviar' if lang == 'es' else 'Send'
    name = 'Nombre' if lang == 'es' else 'Name'
    title_form = 'Rellena los datos para añadir tu proyecto' if lang == 'es' else 'Fill in the details to add your project'
    if request.method == 'POST':
        name_form = request.form['name']
        province = request.form['province']
        start_date = datetime.strptime(request.form['start-date'], '%Y-%m-%d').date()
        budget = Decimal(request.form['budget'])
        insert_new_project_client(id_client, name_form, province, start_date, budget)
        return redirect(url_for('login_client.session_client', id_client=id_client))

    return render_template('logins_sessions/add_project_client.html', data=data, historial=historial,
                           send=send, name=name, title_form=title_form)

@login_client.route('/session/cliente/<int:id_client>/view_info')
def view_info_client(id_client):
    lang = g.language
    data = get_info_client(id_client)
    historial = get_projects_client(id_client, lang)
    view_data_title = 'Datos' if lang == 'es' else 'Data'
    view_data = ['Nombre', 'Apellidos','Usuario', 'Email', 'Direccion', 'Telefono', 'Provincia', 'Fecha registro'] if lang == 'es' \
        else ['Name', 'Surnames', 'Username', 'Email', 'Direction', 'Mobile phone', 'Province', 'Registration date']
    return render_template('logins_sessions/view_info_client.html', data=data, historial=historial,
                           view_data_title=view_data_title, view_data=view_data)

@login_client.route('/session/cliente/<int:id_client>/update_info', methods=['POST', 'GET'])
def update_info_client(id_client):
    lang = g.language
    data = get_info_client(id_client)
    historial = get_projects_client(id_client, lang)
    update_data_title = 'Actualizar datos' if lang == 'es' else 'Update data'
    update_data = ['Nombre', 'Apellidos', 'Usuario', 'Email', 'Direccion', 'Telefono', 'Provincia'] if lang == 'es' \
        else ['Name', 'Surnames', 'Username', 'Email', 'Direction', 'Mobile phone', 'Province']
    update_data_password_title = 'Cambiar contraseña' if lang == 'es' else 'Change password'
    update_data_password = ['Contraseña actual', 'Nueva contraseña', 'Repetir Nueva contraseña'] if lang == 'es' \
        else ['Actual password', 'New password', 'Repeat new password']
    send = 'Enviar' if lang == 'es' else 'Send'

    if request.method == 'POST' and request.form['form_type'] == 'form_update':
        name = request.form['name']
        surnames = request.form['surnames']
        username = request.form['username']
        email = request.form['email']
        direction = request.form['direction']
        phone = request.form['phone']
        province = request.form['province']
        update_data_client(id_client, name, surnames, username, email, direction, phone, province)
        return redirect(url_for('login_client.session_client', id_client=data['id']))

    if request.method == 'POST' and request.form['form_type'] == 'form_update_password':
        actual_password = request.form['actual']
        new_password = request.form['new']
        if check_password_hash(data['password'], actual_password):
            hash_new_password = generate_password_hash(new_password)
            update_password_client(id_client, hash_new_password)
            return redirect(url_for('login_client.session_client', id_client=data['id']))
        else:
            error_password = 'La contraseña actual es incorrecta' if lang == 'es' else 'Actual password is incorrect'
            flash(error_password, 'error_password_2')
            return redirect(url_for('login_client.update_info_client', id_client=data['id']))

    return render_template('logins_sessions/update_info_client.html', data=data, historial=historial,
                           update_data_title=update_data_title, update_data=update_data, update_data_password=update_data_password,
                           update_data_password_title=update_data_password_title, send=send)
