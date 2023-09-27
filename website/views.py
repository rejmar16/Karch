from django.shortcuts import render, get_object_or_404
from .models import Project, Project_Photo, Contact

# Create your views here.

def contact_list(request):
    cont = Contact.objects.first()
    return render(request, 'contact_list.html', {'cont' : cont})

def home(request):
    pr_list = Project.objects.order_by('-published_date')
    return render(request, 'home.html', {'pr_list' : pr_list, 'type':'ALL'})

def RD_detail(request, pk, ip):
    post = get_object_or_404(Project, pk=pk)
    photos = Project_Photo.objects.filter(rodinny_dum=pk).order_by('number')
    ip = int(ip)
    pk = int(pk)
    return render(request, 'RD_detail.html', {'post' : post , 'photos' : photos, 'ip' : ip, 'pk' : pk})

def RD_filter(request, type):
    pr_list = Project.objects.order_by('-published_date')
    type = str(type)
    return render(request, 'home.html', {'pr_list' : pr_list, 'type': type})