from django.urls import path

from . import views

urlpatterns = [
    path('',views.all_squirrels),
    path('add/', views.add, name = 'add'),
    path('stats/', views.stats, name = 'stats'),
    path('<unique_squirrel_id>/', views.update, name = 'update'),
    ]
