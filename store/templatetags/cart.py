from django import template

register=template.Library()

@register.filter(name='product_is_in_cart')
def product_is_in_cart(product,Cart):    
    Keys=Cart.keys()    
    for id in Keys:
         if str(product.id) == id:
            return True
    return False
    
@register.filter(name='cart_quantity')
def cart_quantity(product,cart):    
    Keys=cart.keys()   
    for id in Keys:
         if str(product.id) == (id):
            return cart.get((id))
    return 0

@register.filter(name='price_total')    
def price_total(product,cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name='total_amount_of_cart')    
def total_amount_of_cart(product,cart):
    sum=0
    
    for p in product:
        sum+= price_total(p,cart)
    
    return sum


@register.filter(name='total_quantity')    
def total_quantity(product,cart):
    sum=0
    
    for p in product:
        sum+= cart_quantity(p,cart)
    
    return sum
