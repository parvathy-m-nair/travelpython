

from django.http import HttpResponse
from django.shortcuts import render

from .models import Picture ,Place
# Create your views here.
def view_items(request):
     place=Place.objects.all()
     picture=Picture.objects.all()
     context={
         'places':place,
         'pictures':picture
     }
     return render(request, 'index.html', context)

























# def demo(request):
#     obj=place.objects.all()
#
#
#     return render (request,"index.html",{'result':obj})
# def addimg(request):
#     obj1 = picture.objects.all()
#     return render (request,'index.html',{'image':obj1})


#




# def img(request):

#     return render(request,'index.html',{'value':val})


