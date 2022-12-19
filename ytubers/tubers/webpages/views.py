from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    slider = Slider.objects.all()
    team = Team.objects.all()
    ytuber = Youtuber.objects.all().order_by('-created_at')
    is_featured_ytuber = Youtuber.objects.filter(is_featured=True)
    data = {
        "slider" : slider,
        "team" : team,
        "ytuber" : ytuber,
        "is_featured_ytuber" : is_featured_ytuber
    }
    return render(request, 'webpages/home.html', data )

def about(request):
    return render(request, "webpages/about.html")

def contact(request):
    return render(request, "webpages/contact.html")

def services(request):
    return render(request, "webpages/services.html")