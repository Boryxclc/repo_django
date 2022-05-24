from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.inicio),
    path('familia/', views.familia),
    path('lista_familia/', views.lista_familia),
    path('altaf/', views.altaf),
]
