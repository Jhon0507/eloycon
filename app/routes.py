import os
import random
from flask import render_template, Blueprint, request, g, session, redirect, url_for, current_app
from .query import *
from .project_categories import get_name_for_url_imgs

main = Blueprint('main', __name__)

# define global variables
@main.before_request
def get_variables_before_request():
    lang_from_url = request.args.get('lang')
    if lang_from_url in ['es', 'en']:
        session['lang'] = lang_from_url

    # Usa directamente lo que haya en la sesión (si existe)
    language = session.get('lang', 'es')
    g.language = language
    g.translate = get_values_nav(language)
    g.phrases_carrusel = get_phrases_to_carrusel(language)

    path = os.path.join(current_app.static_folder, 'img', 'carrusel')
    g.img = os.listdir(path)

# inherit global variables for every endpoint
@main.context_processor
def inherit_global_variables():
    return dict(
        lang=g.get('language', 'es'),
        translate=g.get('translate', {}),
        phrases_carrusel=g.get('phrases_carrusel', []),
        img=g.get('img', [])
    )

@main.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['es', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))

@main.route('/')
@main.route('/home')
def home():
    language = g.language
    # section our qualities
    text_q = get_title_description_our_qualities(language)
    text_qualities = get_phrases_our_qualities(language)

    # section our process
    text_process = get_title_description_our_process(language)
    content_process = get_content_our_process(language)

    # section last projects
    title = get_title_last_projects(language)

    # from de last projects take random photo and will change when we reload section home
    last_projects = get_urls_for_last_projects()
    for i in last_projects:
        last_projects[i] = random.choice(last_projects[i])

    # section footer
    footer = get_values_footer(language)
    return render_template('home.html',
                           text_q=text_q,
                           text_qualities=text_qualities,
                           text_process=text_process,
                           content_process=content_process,
                           title=title, # last projects
                           last_projects=last_projects,
                           footer=footer,)


@main.route('/projects')
@main.route('/proyectos')
def proyectos():
    language = g.language
    content = get_title_description_projects(language)  # get title and description
    interiors = get_content_interior(language)  # get img and content for interior section
    exteriors = get_content_exterior(language)  # get img and content for exterior section
    footer = get_values_footer(language)  # load values footer
    return render_template('proyectos.html',
                           content=content,
                           interiors=interiors,
                           exteriors=exteriors,
                           footer=footer
                           )

@main.route('/projects/<section>')
@main.route('/proyectos/<section>')
def seccion_proyectos(section):
    language = g.language
    # every img of project have a type, ej: dormitorio, cerca..., get all the projects that type is same os <section>
    name_to_url = get_name_for_url_imgs(section)
    projects = get_values_for_every_project(name_to_url, language)

    title = get_title_for_every_project(language, section)

    # get the path and imgs for every carrusel type
    path_projects = f'img/carrusel-categories-projects/{name_to_url}'
    imgs_for_every_path = os.listdir(os.path.join(current_app.static_folder, 'img', 'carrusel-categories-projects', name_to_url))
    imgs = [path_projects+'/'+img for img in imgs_for_every_path]

    footer = get_values_footer(language)  # load values footer

    return render_template('proyecto_category.html',
                           title=title,
                           imgs=imgs,
                           projects=projects,
                           footer=footer)

@main.route('/project/<int:id_proyecto>')
@main.route('/proyecto/<int:id_proyecto>')
def proyecto(id_proyecto):
    language = g.language

    content = get_info_of_project(id_proyecto, language)  # get all the content for the selected project
    random_img = random.choice(content['url'])
    footer = get_values_footer(language)  # load values footer
    return render_template('proyecto.html',
                           content=content,
                           random_img = random_img,
                           footer=footer)


@main.route('/us')
@main.route('/nosotros')
def nosotros():
    language = g.language
    titles_us = get_titles_us(language)  # get all titles
    content_1 = get_content_us_1(language)  # get content section 1
    content_2 = get_content_us_2(language)  # get content section 2
    content_3, title_content_us_3  = get_content_us_3(language)  # get content section 3
    content_4 = get_content_us_4(language)
    footer = get_values_footer(language)  # load values footer
    return render_template('nosotros.html',
                           titles_us=titles_us,
                           content_1=content_1,
                           content_2=content_2,
                           title_content_us_3 = title_content_us_3,
                           content_3=content_3,
                           content_4=content_4,
                           footer=footer)

@main.route('/services')
@main.route('/servicios')
def servicios():
    language = g.language

    content = get_all_content_services(language)
    # load values footer
    footer = get_values_footer(language)
    return render_template('servicios.html',
                           content=content,
                           footer=footer)

@main.route('/contact')
@main.route('/contacto')
def contacto():
    language = g.language
    content = get_all_content_contact(language)
    return render_template('contacto.html', content=content)