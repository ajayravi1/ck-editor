from django.urls import path

from . views import *

app_name = 'editor'

urlpatterns = [
    path("", index, name="index"), 
]
