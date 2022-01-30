from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'monacc/index.html')

def seconde(request):
    return render(request, 'monacc/sec.html')
