from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request, 'catalog/catalog.html')
