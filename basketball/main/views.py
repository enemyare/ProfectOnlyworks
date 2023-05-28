from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render,redirect
from .models import *

from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html') #вызываем хтлм шаблон
def about(request):
    return render(request, 'main/about.html')
def portfolio(request):
    return render(request, 'main/portfolio.html')
def profile(request):
    return render(request, 'main/profile.html')

def registration(request):
    form = UserRegisterForm()
    context = {'form': form}
    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Вы успешно зарегестрировались')
    #         return redirect('sign')
    #     else:
    #         messages.error(request, 'ошибка регистрации')
    # else:
    #     form = UserRegisterForm()
    return render(request, 'main/registration.html', context)
def sign(request):
    return render(request, 'main/sign.html')
def team(request):
    return render(request, 'main/team.html')


