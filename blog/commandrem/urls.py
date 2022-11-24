from django.urls import path
from . import views

urlpatterns = [
    path("" , views.CmdRem.as_view() , name="cmdrem"),
]
