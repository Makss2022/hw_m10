from django import template

from ..models import Quote, Tag

register = template.Library()


def tags(quote: Quote):
    tags_list = []
    for tag in quote.tags.all():
        tag: Tag
        tags_list.append(tag.name)
    return tags_list


register.filter('tags', tags)
