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
    return render_template('home.html')

@main.route('/projects')
@main.route('/proyectos')
def proyectos():
    return 'seccion de proyectos'

@main.route('/us')
@main.route('/nosotros')
def nosotros():
    return 'seccion de nosotros'

@main.route('/services')
@main.route('/servicios')
def servicios():
    return 'seccion de servicios'

@main.route('/contact')
@main.route('/contacto')
def contacto():
    return 'seccion de contactos'