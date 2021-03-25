from django import template
from django.db.models import Count
from django.urls import reverse

from posts.models import Category

register = template.Library()


@register.filter
def is_active_link(link, cur_link):
    return 'active' if link == cur_link else ''


@register.inclusion_tag('tags/_sidebar.html')
def sidebar(request):
    categories = Category.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {'categories': categories, 'url': request.get_full_path()}


@register.inclusion_tag('tags/_navbar.html')
def navbar(request):
    urls = {
        'index': reverse('index'),
        'add_post': reverse('add_post'),
    }
    return {'url': request.get_full_path(), 'urls': urls}


@register.inclusion_tag('tags/_post_card.html')
def post_card(post, request, trunc=True):
    return {'request': request,'post': post, 'trunc': trunc}
