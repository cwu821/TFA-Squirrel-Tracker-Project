from django.shortcuts import render

from django.http import HttpResponse

from .models import Squirrels

def index(request):
    squirrels = Squirrels.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'map/index.html', context)
# Create your views here.
