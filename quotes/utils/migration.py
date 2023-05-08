# data transfer from mongoDB to postgresDB

from mongoengine import *
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quotesapp.models import Author, Tag, Quote  # noqa

connect(
    host=f"""mongodb+srv://userweb10:567234@cluster0.j0x5fei.mongodb.net/hw_m09?retryWrites=true&w=majority""",
    ssl=True
)

# ddata models  by MongoEngine:


class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    quote = StringField()
    author = ReferenceField(Authors)
    tags = ListField(StringField(max_length=50))


# migration:
authors = Authors.objects()
for author in authors:
    Author.objects.get_or_create(
        fullname=author.fullname,
        born_date=author.born_date,
        born_location=author.born_location,
        description=author.description
    )

quotes_mng = Qoutes.objects()
for quote_mng in quotes_mng:
    tags_obj = []
    for tag in quote_mng.tags:
        t = Tag.objects.get_or_create(name=tag)[0]
        tags_obj.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote_mng.quote)))
    if not exist_quote:
        author_mng = Authors.objects(pk=quote_mng.author.pk)[0]
        author_djugo = Author.objects.get(fullname=author_mng.fullname)
        quote_djungo = Quote.objects.create(
            quote=quote_mng.quote,
            author=author_djugo
        )
        for tag in tags_obj:
            quote_djungo.tags.add(tag)
