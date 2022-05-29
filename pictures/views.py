from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    images=Image.objects.all()


    return render(request, 'index.html',{'images':images
    })


def search_category(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"image":searched_images})

    else:
        message = "You haven't searched for Image Category"
        return render(request,'search.html',{"message":message})

    # if 'images' in request.GET and request.GET["images"]:
    #     search_term = request.GET.get("images")
    #     searched_images = Image.search_by_category(search_term)
    #     message = f"{search_term}"
        

    #     return render(request, 'search.html',{"message":message,"images": searched_images})

    # else:
    #     message = "You haven't searched for any image by the category name"
    #     return render(request, 'search.html',{"message":message})