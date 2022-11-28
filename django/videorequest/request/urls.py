from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="index"),
    path('requests/', views.vrequest ,name="vrequest")
]
