from django.shortcuts import render
from.models import Place
from .models import Placed

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    newobj = Placed.objects.all()
    return render(request,'index.html',{'result':obj,'new':newobj})
