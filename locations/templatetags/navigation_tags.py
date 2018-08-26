from django import template

from wagtail.core.models import Page

 


register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return context['request'].site.root_page

 
