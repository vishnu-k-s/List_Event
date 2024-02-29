from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Events

# def home(request):
#     return HttpResponse('HOME')


def home(request):
    #return render(request, 'hom.html')
    events = Events.objects.all().order_by('-id')

    paginator = Paginator(events, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'events/home.html', {"page_obj": page_obj})
