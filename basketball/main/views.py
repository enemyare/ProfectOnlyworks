from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView

from .forms import LoginForm, RegisterForm



# Create your views here.
def index(request):
    return render(request, 'main/index.html') #вызываем хтлм шаблон

def myteam(request):
    return render(request, 'main/myteam.html')

def about(request):
    return render(request, 'main/about.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def profile(request):
    return render(request, 'main/profile.html')

class RegiserView(TemplateView):
    template_name = 'main/registration.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form': user_form}
        return render(request,'main/registration.html', context)
    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, 'main/registration.html', context)
def sign(request):
    context = {'login_form': LoginForm()}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь с именем {username} и паролем не был найден!'
                }
        else:
            context = {
                'login_form': login_form,
            }
    return render(request, 'main/sign.html', context)

def team(request):
    return render(request, 'main/team.html')

def logout_user(request):
    logout(request)
    return redirect('index')



