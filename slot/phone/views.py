from django.shortcuts import render


# Create your views here.
  
def index(request):
    return render(request,'index.html')

def simple(request):
    return render(request,'simple.html')

def complex(request):
    return render(request,'complex.html')

# def index(request):
#     return HttpResponse("<h1> God remains the Greatest<h1/>")