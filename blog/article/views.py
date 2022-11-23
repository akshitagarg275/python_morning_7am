from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , "home.html" )


def article(request):
    context = {
        'data' : "Python Django Articles" 
    }
    return render(request, "article/article.html", context)