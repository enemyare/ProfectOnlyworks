from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ''
    }

    return render(request, 'main/index.html') #вызываем хтлм шаблон

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')