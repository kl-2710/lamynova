from django.shortcuts import render
from .models import VisitLog

def dashboard_view(request):
    context = {
        'visit_count': VisitLog.objects.count(),
        
    }
    return render(request, 'dashboard/dashboard.html', context)
# Create your views here.
