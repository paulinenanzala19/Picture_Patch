from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    images=Image.objects.all()
    # category=Category.objects.all()

    # if 'category' in request.GET and request.GET['category']:
    #     cate = request.GET.get('Category')
    #     images = Image.display_category(cate)

    # else:
    #     message = "You haven't searched for any image by the category name"
       


    return render(request, 'index.html',{'images':images
    })

def image_location(request,location):
    images=Image.filter_by_location(location)
    return render(request, 'location.html', {'image_location': images})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Image.search_image_cat(search_term)
        message = f"{search_term}"
        print(searched_images)

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image by the category name"
        return render(request, 'search.html',{"message":message})