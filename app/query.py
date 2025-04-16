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

# GET QUERIES TO BASE.HTML
def get_values_nav(language):
    if language not in ['es', 'en']:
        return 'Language not supported'

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "nav_%"')
    values = cursor.fetchall()
    return {i['clave']:i['texto'] for i in values}

def get_phrases_to_carrusel(language):
    if language not in ['es', 'en']:
        return 'Language not supported'

    cursor = con.cursor(dictionary=True)
    cursor.execute(f'SELECT clave, {language} AS texto FROM traducciones WHERE clave LIKE "frase_carrusel%"')
    phrases = cursor.fetchall()
    return {i['clave']:i['texto'] for i in phrases}
