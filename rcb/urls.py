from django.urls import path
from rcb.views import *
app_name='sai'
urlpatterns=[
    path('virat/',virat,name='virat'),
]