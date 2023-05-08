from datetime import datetime
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .forms import AuthorForm, QuoteForm
from .models import Author, Quote

# Create your views here.

def main(request, page=1):
    quotes = Quote.objects.all()
    pur_page = 10
    paginator = Paginator(quotes, pur_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotesapp/index.html', context={'quotes': quotes_on_page})


def author(request, author_fullname: str):
    author = Author.objects.filter(fullname=author_fullname)[0]
    return render(request, 'quotesapp/author.html', {'author': author})


def add_author(request):
    if request.method == 'POST':     
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()

            date_str = author.born_date
            date_ = datetime.strptime(date_str, '%Y-%m-%d')
            date_new_str = datetime.strftime(date_, '%B %d, %Y')
            author.born_date = date_new_str
            author.save()

            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_author.html', {'form': form})
    return render(request, 'quotesapp/add_author.html', context={'form': AuthorForm()})


def add_quote(request):
    if request.method == 'POST':
        
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/add_quote.html', {'form': form})
    
    return render(request, 'quotesapp/add_quote.html', context={'form': QuoteForm()})
