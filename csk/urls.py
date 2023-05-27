from django.urls import path
from csk.views import *
app_name='sanju'
urlpatterns=[
    path('msd/',msd,name='msd'),
]