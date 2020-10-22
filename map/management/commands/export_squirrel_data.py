import csv
from django.core.management.base import BaseCommand, CommandError
#from django.apps import apps

from map.models import Squirrels

class Command(BaseCommand):
    help = ("Output the specified model as csv")

    def add_arguments(self, parser):
        parser.add_argument('args',type=str,nargs='*')

    def handle(self,*args,**kwargs):
        #path = args[0]
        #fields = Squirrels._meta.fields
        
        #model = apps.get_model('map','Squirrrels')
        field_names = [f.name for f in Squirrels._meta.fields]
        filename = args[0]

        with open(filename, 'w') as fp:
            writer = csv.writer(fp, delimiter = ',')
            writer.writerow(field_names)

            for instance in Squirrels.objects.all():
                writer.writerow([str(getattr(instance,f)) for f in field_names])
