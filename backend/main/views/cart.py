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
                self.cart[producto_id] += quantity * ingrediente.cantidad
            else:
                self.cart[producto_id] = quantity * ingrediente.cantidad
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
        return total

    def get_prods(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use ids to lookup products in database model
        porducts = Producto.objects.filter(id__in = product_ids)
        #Return those looked up products
        return porducts