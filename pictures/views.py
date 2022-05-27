from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    title='Zoomin'
    images=Images.object.all()
    location=Location.object.all()
    category=Category.object.all()

    return render(request,'index.html',{'images':images,'location':location,'category':category,'title':title})

def image_location(request,location):
    images=Image.filter_by_location(location)
    return render(request, 'location.html', {'image_location': images})