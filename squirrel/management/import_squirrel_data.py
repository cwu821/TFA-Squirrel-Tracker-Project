import csv
import datetime

from django.core.management.base import BaseCommand, CommandError

from map.models import Squirrels




class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        path = kwargs['path']

        
        try:
            with open(path, encoding='utf-8') as fp:
                reader = csv.DictReader(fp)
                data = list(reader)

                for item in data:
        
                    squirrel=Squirrels(
                    longitude=item['X'],
                    latitude=item['Y'],
                    unique_squirrel_id=item['Unique Squirrel ID'],
                    shift=item['Shift'],
                    date=datetime.datetime.strptime(
                        item['Date'].strip(), '%m%d%Y').date(),
                    age=item['Age'],
                    primary_fur_color=item['Primary Fur Color'],
                    location=item['Location'],
                    specific_location=item['Specific Location'],
                    running=str_to_bool(item['Running']),
                    chasing=str_to_bool(item['Chasing']),
                    climbing=str_to_bool(item['Climbing']),
                    eating=str_to_bool(item['Eating']),
                    foraging=str_to_bool(item['Foraging']),
                    other_activities=str_to_bool(item['Other Activities']),
                    kuks=str_to_bool(item['Kuks']),
                    quaas=str_to_bool(item['Quaas']),
                    moans=str_to_bool(item['Moans']),
                    tail_flags=str_to_bool(items['Tail flags']),
                    tail_twitches=str_to_bool(item['Tail twitches']),
                    approaches=str_to_bool(item['Approaches']),
                    indifferent=str_to_bool(item['Indifferent']),
                    runs_from=str_to_bool(item['Runs from']),
            )
        
                squirrel.save()
                print(f"Squirrel {item['Unique Squirrel ID']} imported successfully!")
        except:
             raise ValueError("Something is wrong with the data!")
