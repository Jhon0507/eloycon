from pprint import pprint

import mysql.connector
from dotenv import load_dotenv
import os
from googletrans import Translator
import json

load_dotenv() # load environment variables

con=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE')
)

translator = Translator()

def verify_language(language):
    if language not in ['es', 'en']:
        raise ValueError('Language not supported')


# GET QUERIES TO BASE.HTML
def get_values_nav(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nav_%"')
    values = cursor.fetchall()
    return {i['clave']:i['texto'] for i in values}


def get_phrases_to_carrusel(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "frase_carrusel%"')
    phrases = cursor.fetchall()
    return {i['clave']:i['texto'] for i in phrases}


# GET QUERIES TO HOME.HTML
def get_title_description_our_qualities(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave in ("home_cualidades_titulo", "home_cualidades_texto")')
    content = cursor.fetchall()
    return {i['clave']:i['texto'] for i in content}


def get_phrases_our_qualities(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "home_cualidades___"')
    text = cursor.fetchall()
    structured_text = {}

    for i in text:
        key = i['clave']
        suffix = key[-1]  # '1', '2', '3'
        is_title = key[-2] == 't'

        quality_key = f'home_qualities_{suffix}'

        if quality_key not in structured_text:
            structured_text[quality_key] = {}

        if is_title:
            svgs = {'1': 'constructor.svg', '2': 'organization.svg', '3': 'personalization.svg'}
            structured_text[quality_key]['svg'] = svgs.get(suffix, '')
            structured_text[quality_key]['title'] = i['texto']
        else:
            structured_text[quality_key]['description'] = i['texto']
    return structured_text


def get_title_description_our_process(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave in ("home_proceso_titulo", "home_proceso_descripcion")')
    content = cursor.fetchall()
    return {i['clave']:i['texto'] for i in content}


def get_content_our_process(language):
    verify_language(language)

    path_img = 'app\\static\\img\\img-to-web\\home\\img-process'
    img = os.listdir(path_img)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "home_proceso_t_"')
    titles = cursor.fetchall()

    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "home_proceso_d_"')
    description = cursor.fetchall()

    content = {}
    cont = 0

    for i,t,d in zip(img, titles, description):
        cont += 1
        content['home_proceso_'+str(cont)] = {'img': i, 'title': t['texto'], 'description': d['texto']}

    return content


def get_title_last_projects(language):
    verify_language(language)
    cursor = con.cursor()
    cursor.execute(f'SELECT {language} FROM traducciones WHERE clave = "home_ultimos_proyectos_titulo"')
    return cursor.fetchall()[0][0]


# GET QUERIES TO PROYECTOS.HTML
def get_title_description_projects(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave in ("proyecto_titulo", "proyecto_descripcion")')
    content = cursor.fetchall()

    return {i['clave']:i['texto'] for i in content}


def get_content_interior(language):
    verify_language(language)
    path = 'app\\static\\img\\img-to-web\\projects\\interior'
    img = os.listdir(path)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "proyecto_interior%"')
    text = cursor.fetchall()
    # before add the title of the section
    content = {text[0]['clave']:text[0]['texto']}

    for i, t in zip(img, text[1:]):
        content[t['clave']] = {'img': i, 'texto': t['texto']}

    return content


def get_content_exterior(language):
    verify_language(language)
    path = 'app\\static\\img\\img-to-web\\projects\\exterior'
    img = os.listdir(path)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "proyecto_exterior%"')
    text = cursor.fetchall()
    # before add the title of the section
    content = {text[0]['clave']:text[0]['texto']}

    for i, t in zip(img, text[1:]):
        content[t['clave']] = {'img': i, 'texto': t['texto']}

    return content


# GET QUERIES TO PROYECTO_CATEGORY.HTML
def get_name_endpoint():
    cursor = con.cursor()
    cursor.execute(f'SELECT es, en FROM traducciones WHERE clave LIKE "proyecto_interiores__" OR clave LIKE "proyecto_exteriores__" ORDER BY id ASC')
    names = cursor.fetchall()
    names_lowercase = [(es.lower(), en.lower()) for es, en in names]
    return names_lowercase


def get_title_for_every_project(language, section):
    verify_language(language)

    cursor = con.cursor()
    cursor.execute(f'SELECT es, en FROM traducciones WHERE clave LIKE "proyecto_interiores__" OR clave LIKE "proyecto_exteriores__"')
    titles = cursor.fetchall()
    for title in titles:
        if section == title[0].lower() or section == title[1].lower():
            if language == 'es':
                return title[0]
            elif language == 'en':
                return title[1]
    return 'wrong title'


def get_values_for_every_project(type_name, language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT p.id, nombre, url, tipo FROM proyectos p JOIN imagenes_proyectos i ON p.id = i.id_proyecto WHERE i.tipo = "{type_name}"')
    projects = cursor.fetchall()
    content = {}
    for project in projects:
        key = f'proyecto-{project["id"]}'
        if key not in content:
            cursor.execute(f'SELECT i.tipo FROM proyectos p JOIN imagenes_proyectos i ON p.id = i.id_proyecto WHERE p.id = {project['id']}')
            types = cursor.fetchall()
            content[key] = {'id': project['id'],
                            'name': project['nombre'],
                            'type': list(sorted(set([i['tipo'] for i in types]))),
                            'url': [project['url'].replace('app/static/', '')]}
        else:
            content[key]['url'].append(project['url'].replace('app/static/', ''))

    if language == 'en':
        with open('app/json/name_projects.json', 'r', encoding='utf-8') as filename:
            names = json.load(filename)
        with open('app/json/type_name_category_projects.json', 'r', encoding='utf-8') as filename:
            categories = json.load(filename)

        for info in content:
            list_types = []
            for i in content[info]['type']:
                list_types.append(categories[i])
            content[info]['type'] = list_types

        for name in names:
            for info in content:
                if names[name]['es'] == content[info]['name']:
                    content[info]['name'] = names[name]['en']
    return content

# GET QUERIES TO PROYECTO.HTML
def get_info_of_project(id_project, language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT p.id, p.nombre, p.ciudad, t.{language}, i.url '
                   f'FROM proyectos p '
                   f'JOIN traducciones t ON p.id = t.id_proyecto '
                   f'JOIN imagenes_proyectos i ON p.id = i.id_proyecto '
                   f'WHERE p.id = {id_project} AND p.estado = "Terminado"')
    values_query = cursor.fetchall()
    values = {'id': None, 'title': None, 'city': None, 'url':[], 'description': []}
    for value in values_query:
        if values['id'] is None:
            values['id'] = value['id']
        if values['title'] is None:
            values['title'] = value['nombre']
        if values['city'] is None:
            values['city'] = value['ciudad']
        if value[language] not in values['description']:
            values['description'].append(value[language])
        if value['url'] not in values['url']:
            values['url'].append(value['url'].replace('app/static/', ''))

    values['url'] = list(sorted(set(values['url'])))

    if language == 'en':
        with open('json/name_projects.json', 'r', encoding='utf-8') as filename:
            titles = json.load(filename)
        for title in titles:
            if titles[title]['es'] == values['title']:
                values['title'] = titles[title]['en']

    return values

# GET QUERIES TO NOSOTROS.HTML
def get_titles_us(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nosotros___titulo"')
    content = cursor.fetchall()
    return {i['clave']:i['texto'] for i in content}


def get_content_us_1(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nosotros_1_d%"')
    content = cursor.fetchall()
    return {i['clave']:i['texto'] for i in content}


def get_content_us_2(language):
    verify_language(language)

    path = 'app\\static\\img\\img-to-web\\us\\our-history'
    images = os.listdir(path)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nosotros_2_d_"')
    text = cursor.fetchall()

    content = {}
    for i,t in zip(images, text):
        content[t['clave']] = {'texto':t['texto'], 'img': i}
    return content


def get_content_us_3(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute('SELECT nombre, apellidos, profesion, url_foto FROM empleados WHERE id NOT IN (1)')
    employees_consulta = cursor.fetchall()

    name_block_profesion = ['Lideres', 'Arquitectos e Ingenieros', 'Equipo General'] if language == 'es' else ['Leadership Team', 'Architects and Engineers', 'General Team']

    employees = {'leadership-team': {}, 'architects-engineers': {}, 'general-team': {}}
    cont = 0

    # have all profesion in one string to do a request to API translator only one time
    profession_text = "\n".join([employee['profesion'] for employee in employees_consulta])
    translate_professions_text = translator.translate(profession_text, dest=language).text

    # return to list all the professions
    translate_professions = translate_professions_text.split("\n")

    for employee, translate_profession in zip(employees_consulta, translate_professions):
        cont += 1
        team = employee['url_foto'].split('/')[-2]

        employee_data = {
            'name': f'{employee['nombre']} {employee['apellidos']}',
            'profession': translate_profession,
            'url': employee['url_foto'].replace('app/static/', '')
        }

        if team in employees:
            employees[team][f'employee{cont}'] = employee_data

    return employees, name_block_profesion


def get_content_us_4(language):
    verify_language(language)

    path = 'app\\static\\img\\img-to-web\\us\\corporate-social-responsibility'
    svgs = os.listdir(path)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nosotros_4_t_"')
    content_title_query = cursor.fetchall()

    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nosotros_4_d_"')
    content_description_query = cursor.fetchall()

    content = {}
    cont = 0

    for title, description, svg in zip(content_title_query, content_description_query, svgs):
        cont += 1
        content[f'content-{cont}'] = {
            'title': title['texto'],
            'description': description['texto'],
            'url': f'img/img-to-web/us/corporate-social-responsibility/{svg}'
        }

    return content


# QUERY FOR FOOTER
def get_values_footer(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "footer%"')
    content = cursor.fetchall()
    return {i['clave']:i['texto'] for i in content}
