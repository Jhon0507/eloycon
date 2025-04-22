import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv() # load environment variables

con=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE')
)

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
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "home_cualidades%"')
    text = cursor.fetchall()
    structured_text = {}
    for i in text:
        if i['clave'][-1] == '1':
            if i['clave'][-2] == 't':
                structured_text['home_qualities_1'] = {'svg': 'constructor.svg'}
                structured_text['home_qualities_1'].update({'title': i['texto']})
            else: structured_text['home_qualities_1'].update({'description': i['texto']})
        elif i['clave'][-1] == '2':
            if i['clave'][-2] == 't':
                structured_text['home_qualities_2'] = {'svg': 'organization.svg'}
                structured_text['home_qualities_2'].update({'title': i['texto']})
            else: structured_text['home_qualities_2'].update({'description': i['texto']})
        elif i['clave'][-1] == '3':
            if i['clave'][-2] == 't':
                structured_text['home_qualities_3'] = {'svg': 'personalization.svg'}
                structured_text['home_qualities_3'].update({'title': i['texto']})
            else: structured_text['home_qualities_3'].update({'description': i['texto']})
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

# QUERY FOR FOOTER
def get_values_footer(language):
    verify_language(language)

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "footer%"')
    content = cursor.fetchall()
    return {i['clave']:i['texto'] for i in content}
