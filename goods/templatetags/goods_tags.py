
from urllib.parse import urlencode
from django import template
from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kworgs):
    query = context['request'].GET.dict()
    query.update(kworgs)
    return urlencode(query)