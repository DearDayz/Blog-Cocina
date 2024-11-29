from blog.models import Ingrediente
from ecommerce.models import Producto
from decimal import Decimal
class Cart():
    def __init__(self, request):
        self.session = request.session

        #Obtiene la actual clave de sesion si existe
        cart = self.session.get('session_key') #Este valor lo estamos imponiendo nosotros, no lo trae por default session

        if 'session_key' not in request.session: #Si no existe la clave, la crea
            cart = self.session['session_key'] = {} # Le asigna un diccionario vacio
        self.cart = cart
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def add(self, receta, quantity):
        ingredientes = Ingrediente.objects.filter(receta=receta.id)
        for ingrediente in ingredientes:
            producto_id = str(ingrediente.producto.id)
            if producto_id in self.cart:
                self.cart[producto_id] += round(quantity * ingrediente.cantidad, 2)
            else:
                self.cart[producto_id] = round(quantity * ingrediente.cantidad, 2)
            self.session.modified = True
    def __len__(self):
        return len(self.cart)

    
    def card_total(self):
        #Get product IDS
        product_ids = self.cart.keys()
        #Get products from database model
        products = Producto.objects.filter(id__in=product_ids)
        #Get quantities
        quantities = self.cart
        # Start counting at 0
        total = 0
        for key,value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total += product.precio * Decimal(value)
        return Decimal(total)

    def get_prods(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use ids to lookup products in database model
        porducts = Producto.objects.filter(id__in = product_ids)
        #Return those looked up products
        return porducts
    
    def get_subtotales(self):
        subotatles = {}
        for key,value in self.cart.items():
            key = int(key)
            for product in self.get_prods():
                if product.id == key:
                    subotatles[str(key)] = round(float(product.precio) * value, 2) #product.precio * value
        return subotatles
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        #Get cart
        ourcart = self.cart
        #Update Dictionary/cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        return self.cart
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def clear(self):
        self.session['session_key'] = {}
        self.cart = self.session['session_key']
        self.session.modified = True