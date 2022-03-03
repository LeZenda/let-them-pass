from django.urls import path

from . import views

urlpatterns = [
    path('', views.news, name='index'),
    path('countries/', views.countries, name='countries'),
    path('countries/<int:country_id>/', views.country, name='country'),
    path('crossings/', views.crossings, name='crossings'),
]