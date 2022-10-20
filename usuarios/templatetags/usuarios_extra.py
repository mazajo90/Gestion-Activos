from django import template
from usuarios.models import User

register = template.Library()

@register.simple_tag
def get_up_and_del():
    usuarios = User.objects.all()
    return usuarios
