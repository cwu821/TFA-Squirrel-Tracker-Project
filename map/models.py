from django.db import models
from django.utils.translation import gettext as _
 
class Squirrels(models.Model):
    longitude = models.FloatField(
    	    help_text=_('longitude of squirrels'),
	)  
	
    latitude = models.FloatField(
    	    help_text=_('latitude of squirrels'),
	)	
	
    unique_squirrel_id = models.CharField(
    	    help_text=_('unique id of squirrels'),
    	    max_length=50,
	)
        
    AM='AM'
    PM='PM'

    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM,_('PM')),
    ]

    shift = models.CharField(
            help_text=_('shift choice, AM or PM'),
            choices=SHIFT_CHOICES,
            max_length=2,
            null=True,
    )
        
    date = models.DateField(
	help_text=_('date seen'),
    )

    JUVENILE = 'Juvenile'
    ADULT = 'Adult'

    AGE_CHOICES = [
	    (JUVENILE, _('Juvenile')),
	    (ADULT, _('Adult')),
    ]

    age = models.CharField(
            help_text=_('Age of squirrel'),
	    choices=AGE_CHOICES,
            max_length=50,
            null=True,
    )

    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMON = 'Cinnamon'
    
    COLOR_CHOICES = (
	(BLACK, _('Black')),
	(GRAY, _('Gray')),
	(CINNAMON, _('Cinnamon'))
    )
    
    primary_fur_color = models.CharField(
		help_text = _('Primary fur color'),
		choices = COLOR_CHOICES,
                max_length=50,
                null=True,
	)

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
        

    LOCATION_CHOICES = (
	    (ABOVE_GROUND, _('Above ground')),
	    (GROUND_PLANE, _('Ground plane'))
    )
        
    location = models.CharField(
	    help_text = _('location: above ground or ground plane'),
	    choices = LOCATION_CHOICES,
            max_length=50,
            null=True,
    )

    specific_location = models.CharField(
            help_text = _('Sepecific location'),
            max_length=100,
	    null = True,
            blank = True,
    )
        
    running = models.BooleanField(
	    help_text = _('whether the squirrel is running')
        )
    chasing = models.BooleanField(
            help_text = _('whether the squirrel is chasing')
        )
    climbing = models.BooleanField(
	    help_text = _('whether the squirrel is climbing')
        )
    eating = models.BooleanField(
    	    help_text = _('whether the squirrel is eating')
        )
    foraging = models.BooleanField(
            help_text = _('whether the squirrel is foraging')
        )
    other_activities = models.CharField(
	    help_text = _('other activities'),
	    max_length = 150,
	    null = True,
            blank = True,
        )
    kuks = models.BooleanField(
            help_text = _('kuks sound')
        )

    quaas = models.BooleanField(
	    help_text = _('quaas sound')
        )

    moans = models.BooleanField(
	    help_text = _('moans sound')
        )
    tail_flags = models.BooleanField(
	    help_text = _('whether the squirrel is flagging tail')
        )
    tail_twitches = models.BooleanField(
	    help_text = _('whether the squirrel is twitching tail')
        )
    approaches = models.BooleanField(
	    help_text = _('whether the squirrel is approaching')
        )
        
    indifferent = models.BooleanField(
	    help_text = _('whether the squirrel is indifferent')
        )
    runs_from = models.BooleanField(
    	    help_text = _('whether the squirrel is running away')
        )
        
    def __str__(self):
        return self.unique_squirrel_id



# Create your models here.
