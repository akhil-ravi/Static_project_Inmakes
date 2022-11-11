from django.shortcuts import render
from .models import place
# Create your views here.
def static(request):
    obj = place.objects.all()
    return render(request,'index.html',{'key':obj})
def static1(request):
    return render(request,'static.html')