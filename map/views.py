from django.shortcuts import render

from django.http import HttpResponse

from .models import Squirrels

def index(request):
    squirrels = Squirrels.objects.all()[:80]
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'map/map.html', context)
# Create your views here.
