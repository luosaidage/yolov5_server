from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('add/', views.add, name='add'),
]