from django.urls import path
from  . import views

urlpatterns = [
    path('', views.recuerdos, name="recuerdos"),
    path('historia/', views.historia, name="historia")
    

] 
