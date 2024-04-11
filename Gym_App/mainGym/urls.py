from django.urls import path
from mainGym import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('programma', views.programma, name='programma'),
    path('traning', views.training, name= 'training'),
    path('registr', views.registrating, name='registrated'),
]