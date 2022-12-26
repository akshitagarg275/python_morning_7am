from django.shortcuts import render, get_object_or_404
from .models import Youtuber
# Create your views here.


def youtubers(request):
    ytubers = Youtuber.objects.all()

    data = {
        'ytubers' : ytubers
    }

    return render(request, 'youtubers/ytubers.html', data)

def search(request):
    tubers = Youtuber.objects.all().order_by('-created_at')
    camera_type = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_type = Youtuber.objects.values_list('category',flat=True).distinct()
    city = Youtuber.objects.values_list('city',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword'] 
        # print(request.GET['keyword'])
        tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        tubers = tubers.filter(city__icontains=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        tubers = tubers.filter(camera_type__icontains=camera_type)

    if 'category_type' in request.GET:
        category_type = request.GET['category_type']
        tubers = tubers.filter(category_type__icontains=category_type)

    
    data = {
            'tubers' : tubers,
            'camera_type' : camera_type,
            'category_type' : category_type,
            'city' : city
        }
    # print(data)
    print(city)
    return render(request, 'youtubers/search.html', data)


def youtuber_detail(request, id):
    ytuber = get_object_or_404(Youtuber, pk= id)

    data = {
        "ytuber" : ytuber
    }
    return render(request, 'youtubers/youtubers_detail.html', data)
