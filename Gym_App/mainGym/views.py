from django.shortcuts import render
from .models import Exersises, Calendar
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def home(request):
    return render(request, 'mainGym/home.html',
            {
             
            }
        )

def programma(request):
    all_calendar = Calendar.objects.all()
    return render(request, 'mainGym/programma.html',
            {
                'data_calendar': all_calendar
            }
        )


def training(request):
    all_exersises = Exersises.objects.all()
    return render(request, 'mainGym/training.html',
                {
                    'data_Exersises': all_exersises 
                }
            )


def registrating(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return render(request, "mainGym/home.html")
    else:
        return HttpResponse('User not found')
