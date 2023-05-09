from django.urls import path

from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('author/<str:author_fullname>', views.author, name='author'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('tag/<str:tag>', views.quotes_by_tag, name='quotes_by_tag'),
    path('tag/<str:tag>/<int:page>', views.quotes_by_tag,
         name='quotes_by_tag_paginate'),
]
