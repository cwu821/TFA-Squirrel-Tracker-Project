import csv
import datetime

from django.core.management.base import BaseCommand, CommandError

from map.models import Squirrels

def str_to_bool(x):
    if x.lower() == 'true':
        return True
    elif x.lower() == 'false':
        return False
    else:
            # evil ValueError that doesn't tell you what the wrong value was
        raise ValueError("Has to be True or False!")

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        try:
            with open(path, encoding='utf-8') as fp:
                reader = csv.DictReader(fp)


                for item in reader:
                    squirrel = Squirrels.objects.filter(
                    unique_squirrel_id=item['Unique Squirrel ID'])
                    if squirrel.exists():
                        continue
                    squirrel=Squirrels(
                        longitude=item['X'],
                        latitude=item['Y'],
                        unique_squirrel_id=item['Unique Squirrel ID'],
                        shift=item['Shift'],
                        date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4])),   
                        age=item['Age'],
                        primary_fur_color=item['Primary Fur Color'],
                        location=item['Location'],
                        specific_location=item['Specific Location'],
                        running=str_to_bool(item['Running']),
                        chasing=str_to_bool(item['Chasing']),
                        climbing=str_to_bool(item['Climbing']),
                        eating=str_to_bool(item['Eating']),
                        foraging=str_to_bool(item['Foraging']),
                        other_activities=item['Other Activities'],
                        kuks=str_to_bool(item['Kuks']),
                        quaas=str_to_bool(item['Quaas']),
                        moans=str_to_bool(item['Moans']),
                        tail_flags=str_to_bool(item['Tail flags']),
                        tail_twitches=str_to_bool(item['Tail twitches']),
                        approaches=str_to_bool(item['Approaches']),
                        indifferent=str_to_bool(item['Indifferent']),
                        runs_from=str_to_bool(item['Runs from']),
                    )

                    squirrel.save()
                    #print(f"Squirrel {item['Unique Squirrel ID']} imported successfully!")
        except csv.Error as e:
             print(f'there is something wrong with {reader.line_num}')

        #except:
             #raise ValueError("Something is wrong with the data!")

