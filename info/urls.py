from django.urls import path

from . import views

urlpatterns = [
    path('', views.news, name='index'),
    path('crossings/', views.crossings, name='crossings'),
]