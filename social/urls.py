from django.urls import path, include
from  social import views



urlpatterns = [
    path('', views.estudiantes, name='estudiantes'),
	path('profile/<str:username>/', views.profile, name='profile'),
    path('datos/', views.profile, name='datos'),
    path('notas_parciales/', views.notas, name='notas1'),
    path('notas/<str:username>/', views.notas, name='notas'),
    path('notas_definitivas/', views.notas_definitivas, name='notas'),
    path('notas1/<str:username>/', views.notas_definitivas, name='notas1'),
   
    

]