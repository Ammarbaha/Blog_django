from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/post/lastes_posts.html')
def show_lastes_posts(count=5):
    lastes_posts = Post.objects.order_by('-publish')[:count]
    return {'lastes_posts':lastes_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


