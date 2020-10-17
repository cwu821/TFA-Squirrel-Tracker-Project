from django.urls import path

from . import views

urlpatterns = [
    path('',views.all_squirrels),
    path('<unique_squirrel_id>/', views.update, name = 'update'),
    ]
