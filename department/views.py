from django.shortcuts import render
from django.http import HttpResponse
from .models import Positions

# Create your views here.


def table_view(request):
    poses = Positions.objects.filter(count_person__lt=100)
    name = []
    count = []
    for i in range(len(poses)):
        name.append(poses[i].position)
        count.append(poses[i].count_person)
    return HttpResponse(f'Должность {name}\n Кол-во {count}')
