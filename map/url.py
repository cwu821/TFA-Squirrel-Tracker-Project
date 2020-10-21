from django.url import path
from . import views
	
urlpattern  =  [ 
    path('', views.index), ]

