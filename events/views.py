from django.shortcuts import render
from django.http import HttpResponse

from .models import Events

# def home(request):
#     return HttpResponse('HOME')


def home(request):
    #return render(request, 'hom.html')
    events = Events.objects.all()
   
    return render(request, 'events/home.html', {'events' : events})