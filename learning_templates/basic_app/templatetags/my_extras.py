from django import template

register=template.Library()

@register.filter(name='cutters') # can use this instead of below code
def cutters(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """

    return value.replace(arg,'')

#register.filter('cutters',cutters) #what you want to call it and the function, register it
#can use @register above, better looking
