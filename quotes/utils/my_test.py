import os
import django
from datetime import datetime, date

from django.http import QueryDict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quotesapp.models import Author, Tag, Quote  # noqa
from django.core.paginator import Paginator  # noqa


# quotes = Quote.objects.all()
tag_ = Tag.objects.get(name="love")
quotes = Quote.objects.filter(tags=tag_)
print(quotes, type(quotes))
# pur_page = 10
# paginator = Paginator(quotes, pur_page)
# quotes_on_page = paginator.page(2)
# print(quotes_on_page.previous_page_number())
# print(quotes_on_page.has_previous())

# author = Author.objects.get(pk=50)
# print(author.born_date)
# print(type(author.born_date))

# date_str = author.born_date
# date_ = datetime.strptime(date_str, '%Y-%m-%d')
# date_new_str = datetime.strftime(date_, '%B %d, %Y')
# print(date_new_str)
# print(type(date_new_str))

# d = QueryDict("a=1", mutable=True)
# d.update({"tags": Tag(name="live")})
# d.update({"tags": Tag(name="life")})
# # print(d, type(d))
# # print(d["tags"], type(d["tags"]))
# print(d.get("tags"), type(d.get("tags")))
# # print(d.getlist("tags"), type(d.getlist("tags")[0]))
# # choice_tags = Tag.objects.filter(name__in=d.getlist('tags'))
# # # choice_tags = Tag.objects.filter(name__in=["life"])
# # print(choice_tags)
# tag = Tag.objects.get(name=d.get("tags"))
# print(tag, type(tag))
# for tag in choice_tags:
#     print(tag, type(tag))
# for tag in choice_tags.iterator():
#     print(tag, type(tag))
# tags = Tag.objects.all()
