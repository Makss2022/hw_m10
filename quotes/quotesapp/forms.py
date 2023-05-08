from django.forms import ModelForm, CharField, TextInput, Textarea, DateField, DateInput, ModelChoiceField, Select, SelectMultiple, ModelMultipleChoiceField
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):

    fullname = CharField(min_length=5, max_length=100, widget=TextInput(
        attrs={"type": "text", "class": "form-control", "placeholder": "Fullname"}))
    born_date = DateField(widget=DateInput(
        attrs={"type": "date", "class": "form-control"}))
    born_location = CharField(min_length=5, max_length=150, widget=TextInput(
        attrs={"type": "text", "class": "form-control", "placeholder": "Born location"}))
    description = CharField(min_length=5, max_length=15000, widget=Textarea(
        attrs={"class": "form-control", "style": "height: 112px", "placeholder": "Description"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=3000, widget=Textarea(
        attrs={"class": "form-control", "style": "height: 84px", "placeholder": "Quote"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"), empty_label="Select author", widget=Select(
        attrs={"class": "form-select"}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=False, widget=SelectMultiple(
        attrs={"class": "form-select", "multiple aria-label": "multiple select example"}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
