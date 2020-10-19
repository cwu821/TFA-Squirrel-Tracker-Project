from django.forms import ModelForm

from map.models import Squirrels

class Form(ModelForm):
    class Meta:
        model = Squirrels
        fields = '__all__'
