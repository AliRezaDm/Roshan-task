import psutil
from django.shortcuts import render
from random import randint
from datetime import datetime


def random_color():
    return f"rgb{randint(0, 255), randint(0, 255), randint(0, 255)}"

def system_status(request):

    # Getting cpu and ram precentage
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory()
    time_and_date = datetime.today()

    color =  random_color()
    background = random_color()    

    context = {
        'cpu_usage' : cpu_usage,
        'ram_usage' : ram_usage, 
        'color' : color,
        'background' : background,
        'datetime' : time_and_date
    }

    return render(request, 'main.html', context)