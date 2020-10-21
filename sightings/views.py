from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.db.models import Count

from map.models import Squirrels

from .forms import Form

def all_squirrels(request):
    squirrels = Squirrels.objects.all()
    context = {
        'squirrels': squirrels
    }

    return render(request, 'sightings/all_squirrels.html', context)

def update(request, unique_squirrel_id):
    squirrel = Squirrels.objects.get(unique_squirrel_id=unique_squirrel_id)
    
    if request.method == 'POST':
        form = Form(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    
    else:
        form = Form(instance=squirrel)

    context = {
            'form': form,
    }

    return render(request, 'sightings/update.html', context)

def add(request):
    if request.method == 'POST':
        form = Form(request,POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = Form()

        context = {
            'form': form,
        }

        return render(request, 'sightings/add.html', context)

def stats(request):
    total_count = Squirrels.objects.all().count()
    age_juvenile = Squirrels.objects.filter(age='Juvenile').count()
    age_adult = Squirrels.objects.filter(age='Adult').count()
    location_above = Squirrels.objects.filter(location='Above Ground').count()
    location_plane = Squirrels.objects.filter(location='Ground Plane').count()
    running_true = Squirrels.objects.filter(running=True).count()
    #running_false = Squirrels.objects.filter(running=False).count()
    eating_true = Squirrels.objects.filter(eating=True).count()
    approach_true = Squirrels.objects.filter(approaches=True).count()
    context = {
            'total_count':total_count,
            'age_juvenile': age_juvenile,
            'age_adult': age_adult,
            'location_above': location_above,
            'location_plane': location_plane,
            'running_true': running_true,
            'eating_true': eating_true,
            'approach_true': approach_true,
    }
    return render(request, 'sightings/stats.html',context)

def home(request):
    return render(request, 'sightings/home.html')

#Create your views here.
