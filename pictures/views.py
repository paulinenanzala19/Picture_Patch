from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    title='Zoomin'
    images=Images.object.all()
    location=Location.object.all()
    categories=category.object.all()

    return render(request,'index.html',{'images':images,'location':location,'categories':categories,'title':title})

def location(request, location):
    images=Images.filter_by_location(location)