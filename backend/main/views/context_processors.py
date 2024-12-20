from .cart import Cart
from decimal import Decimal, ROUND_HALF_UP
from blog.models import Category


# Create context processor so our cart can work on all page
def cart(request):
    # Return the deafult data from our Cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.card_total().quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    subtotales = cart.get_subtotales()
    return {"cart": cart,"cart_products": cart_products, "quantities": quantities, "totals": totals ,"subtotales": subtotales}

def categorias(request):
    categorias1 = Category.objects.all()
    categ_dict = {}
    for categoria in categorias1:
        categ_dict[categoria.name.replace(" ", "-")] = categoria.name
    return {"categ_dict": categ_dict, "categorias1": categorias1}