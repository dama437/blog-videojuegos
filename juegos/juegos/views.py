from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Nosotros(request):
    return render(request, 'nosotros.html')