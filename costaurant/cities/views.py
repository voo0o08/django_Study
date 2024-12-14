from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cities/index.html')

def city_detail(request, name):
    context = {"city":name}
    return render(request, f"cities/{name}.html", context=context)


