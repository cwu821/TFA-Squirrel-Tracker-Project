from django.shortcuts import render
from django.shortcuts import get_object_or_404

from map.models import Squirrels

from .forms import UpdateForm

def all_squirrels(request):
    squirrels = Squirrels.objects.all()
    context = {
        'squirrels': squirrels
    }

    return render(request, 'sightings/all_squirrels.html', context)

def update(request, unique_squirrel_id):
    squirrel = Squirrels.objects.get(unique_squirrel_id=unique_squirrel_id)
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}/')
    
    else:
        form = UpdateForm(instance=squirrel)

    context = {
        'squirrel': form,
    }

    return render(request, 'sightings/update.html', context)

#Create your views here.
