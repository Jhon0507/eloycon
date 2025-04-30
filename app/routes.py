from flask import Flask, render_template, Blueprint, request, g
from .query import *
import os

main = Blueprint('main', __name__)
app = Flask(__name__)

# define global variables
@main.before_request
def get_variables_before_request():
    language = request.args.get('lang', 'es')
    # define global variables for every endpoint
    g.language = language
    g.translate = get_values_nav(language)
    g.phrases_carrusel = get_phrases_to_carrusel(language)

    path = os.path.join(app.static_folder, 'img', 'carrusel')
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

@main.route('/')
@main.route('/home')
def home():
    language = request.args.get('lang', 'es')
    # section our qualities
    text_q = get_title_description_our_qualities(language)
    text_qualities = get_phrases_our_qualities(language)

    # section our process
    text_process = get_title_description_our_process(language)
    content_process = get_content_our_process(language)

    # section last projects
    title = get_title_last_projects(language)
    # get images form last projects (review)
    img_last_projects_c = ['construction/project-1/stairsB.webp', 'construction/project-2/movie-theaterB.webp',
                           'construction/project-3/barbecue-areaB.webp', 'construction/project-4/poolB.webp',
                           'construction/project-5/kitchenB.webp', 'construction/project-6/stairsB.webp']
    img_last_projects_r = ['reform/project-1/bathroomB.webp', 'reform/project-2/barbecue-areaB.webp',
                           'reform/project-3/officeB.webp',
                           'reform/project-4/roomB.webp', 'reform/project-5/stairsB.webp']

    # section footer
    footer = get_values_footer(language)
    return render_template('home.html',
                           text_q=text_q,
                           text_qualities=text_qualities,
                           text_process=text_process,
                           content_process=content_process,
                           title=title,
                           footer=footer,
                           img_last_projects_c=img_last_projects_c,
                           img_last_projects_r=img_last_projects_r)

@main.route('/projects')
@main.route('/proyectos')
def proyectos():
    language = request.args.get('lang', 'es')
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


@main.route('/proyectos/<section>')
def seccion_proyectos(section):
    return 'casas'

@main.route('/us')
@main.route('/nosotros')
def nosotros():
    language = request.args.get('lang', 'es')
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
    # load values footer
    footer = get_values_footer(request.args.get('lang', 'es'))
    return render_template('servicios.html',
                           footer=footer)

@main.route('/contact')
@main.route('/contacto')
def contacto():
    # load values footer
    footer = get_values_footer(request.args.get('lang', 'es'))
    return render_template('contacto.html',
                           footer=footer)