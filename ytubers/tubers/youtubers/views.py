from django.shortcuts import render
from .models import Youtuber
# Create your views here.
def search(request):
    tubers = Youtuber.objects.all().order_by('-created_at')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword'] 
        # print(request.GET['keyword'])

        tubers = tubers.filter(description__icontains=keyword)

        data = {
            'tubers' : tubers
        }
        print(data)
    return render(request, 'youtubers/search.html', data)