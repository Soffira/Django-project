from django import template

register = template.Library()

@register.simple_tag  #декоратор превращает функцию в соответствующий template tag
def get_value_by_key(source, key):
    return source.get(key)
    
@register.filter(name='even')
def get_even_items(items):
    return (itm for idx, itm in enumerate(items, 1) if idx % 2 == 0) #фильтр, позволяет вывести на экран только четные элементы