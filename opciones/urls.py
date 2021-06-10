from django.urls import path
from  opciones import views 
from django.conf import settings


urlpatterns = [
    path('', views.primero, name="primero"),
    path('segundo/', views.segundo, name="segundo"),
    path('tercero/', views.tercero, name="tercero"),
    path('cuarto/', views.cuarto, name="cuarto"),
    path('quinto/', views.quinto, name="quinto"),
   

   
    

] 