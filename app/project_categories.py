from app.routes import get_name_endpoint

def get_name_for_url_imgs(section):
    categories = get_name_endpoint()
    # important order list
    name_categories = ['sala de estar', 'cocina', 'dormitorio', 'baño', 'escaleras', 'despacho', 'gym',
                     'sala de cine', 'zona de lavado', 'fachada', 'terraza', 'piscina', 'garaje', 'cerca',
                     'patio', 'area de barbacoa', 'estanque', 'patio de niños']
    for index, category in enumerate(categories):
        if section in category:
            return name_categories[index]
