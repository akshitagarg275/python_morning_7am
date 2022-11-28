from django.shortcuts import render,redirect
from .models import Video
from .forms import VideoForm


def index(request):
    videos = Video.objects.order_by('-date_added')
    data = {
        'videos' : videos
    }

    return render(request, 'request/index.html',data)


def vrequest(request):
    if request.method == 'POST':
        # print("POST REQUEST")
        #user entered form
        form = VideoForm(request.POST)
        # print(form)

        if form.is_valid():
            # print("REQUEST: ",request.POST)
            # print("FORM: ",form)
            # print("videoname: ", request.POST['videoname'])
            # print("videoDesc: ", request.POST['videodesc'])
            new_req = Video(videoTitle = request.POST['videoname'], videoDesc = request.POST['videodesc'])
            new_req.save()
            return redirect('index')

    else:
        # print("First load")
        form = VideoForm()
        # print(form)
    
    data = {
            'form' : form
        }

    return render(request , 'request/vrform.html' , data)
