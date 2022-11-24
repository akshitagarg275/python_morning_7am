from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , "home.html" )


def article(request):
    context = {
        'data' : "Python Django Articles" 
    }
    return render(request, "article/article.html", context)

def detail_article(request):
    return render(request, "article/detail_article.html")

def contact(request):
    return render(request, "article/contact.html")

def about(request):
    return render(request, "article/about.html")