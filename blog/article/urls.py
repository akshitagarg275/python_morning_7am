from django.urls import path
from . import views

urlpatterns = [
    path('article/' , views.article , name="article"),
    path('detail_article/' , views.detail_article , name="detail_article"),
    path('about/' , views.about , name="about"),
    path('contact/' , views.contact , name="contact"),
    path('' , views.home , name="home"),
]
