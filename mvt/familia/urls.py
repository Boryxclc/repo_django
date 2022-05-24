from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.inicio),
    path('familia/', views.familia),
]
