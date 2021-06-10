from django.urls import path
from  . import views

urlpatterns = [
    path('', views.anuncios, name="anuncios"),
    path('promedios/', views.promedios, name="promedios"),
    
    

] 
