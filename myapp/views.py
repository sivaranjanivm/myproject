from django.shortcuts import render
from .models import Gallery

def home(request):
    items = Gallery.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'items': items})