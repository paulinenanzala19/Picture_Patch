from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    # title='Zoomin'
    images=Image.objects.all()
    # location=Location.objects.all()
    # category=Category.objects.all()

    return render(request, 'index.html',{'images':images})
    # 'location':location,'category':category,'title':title})

def image_location(request,location):
    images=Image.filter_by_location(location)
    return render(request, 'location.html', {'image_location': images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_image_cat(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image by the category name"
        return render(request, 'search.html',{"message":message})