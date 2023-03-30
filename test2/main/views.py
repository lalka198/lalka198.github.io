import requests
from django.shortcuts import render
from .models import Task
from .models import City
from .forms import TaskForm
from .forms import CityForm

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



city = ("Самара")
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, "main/index.html", {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, "main/about.html")


def get_weather():

    owm = OWM('9feb6f1834fc871f385edf6ef03f83f9')
    mgr = owm.weather_manager()

    # Search for current weather in London (Great Britain) and get details

    observation = mgr.weather_at_place(city)
    w = observation.weather

    t = w.temperature('celsius')["temp"]  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

    return round(t)

def weather(request):

    context = {
        "temperature": get_weather(),
        "city": city
  }

    return render(request, "main/weather.html", context=context)


def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Данные заполнены неверно"

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, "main/create.html", context)




