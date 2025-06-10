from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def service_1(request):
    return render(request, 'qldichvu/service-1.html')

def service_2(request):
    return render(request, 'qldichvu/service-2.html')

def service_3(request):
    return render(request, 'qldichvu/service-3.html')

def services(request):
    return render(request, 'qldichvu/services.html')

