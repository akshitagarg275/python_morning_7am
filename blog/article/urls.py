from django.urls import path
from . import views

urlpatterns = [
    path('article/' , views.article , name="article"),
    path('' , views.home , name="home"),
]
