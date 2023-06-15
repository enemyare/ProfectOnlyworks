from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
from .models import userProfile, Myteam
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def editmyteam(request):
    return render(request, 'main/editmyteam.html')

def logout_user(request):
    logout(request)
    return redirect('sign')


class RegiserView(View):
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
            q = userProfile(user=user)
            q.save()
            w = Myteam(user=user)
            w.save()
            login(request, user)
            return redirect('editprofile')

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
# @login_required(login_url='login')
def team(request):
    user_profile = userProfile.objects.all().order_by('user')
    context = {
        'profiles': user_profile
    }

    return render(request, 'main/team.html', context)
@login_required(login_url='login')
def myteam(request, username):
    user = User.objects.get(username=username)
    myteamprofile = Myteam.objects.get(user=user)
    if request.method == 'POST':
        Myteam.avatar = request.POST.get('img')
        Myteam.save()
    context = {
        'myteamprofile': myteamprofile
    }

    return render(request, 'main/myteam.html', context)

def editmyteam(request):

    myteamprofile = Myteam.objects.get(user=request.user)
    if request.method == 'POST' and 'text-file' in request.POST:
        myteamprofile.nameteam = request.POST.get('nameteam')
        myteamprofile.player1 = request.POST.get('player1')
        myteamprofile.player2 = request.POST.get('player2')
        myteamprofile.player3 = request.POST.get('player3')
        myteamprofile.player4 = request.POST.get('player4')
        myteamprofile.player5 = request.POST.get('player5')

        myteamprofile.player1pos = request.POST.get('player1pos')
        myteamprofile.player2pos = request.POST.get('player2pos')
        myteamprofile.player3pos = request.POST.get('player3pos')
        myteamprofile.player4pos = request.POST.get('player4pos')
        myteamprofile.player5pos = request.POST.get('player5pos')
        myteamprofile.save()
        return redirect('index')
    elif request.method == 'POST' and 'image-file' in request.POST:
        image = request.FILES.get('image', False)
        if image:
            myteamprofile.image = image
        myteamprofile.save()
        return redirect('index')
    else:
        return render(request, 'main/editmyteam.html', {'myteamprofile': myteamprofile})

@login_required(login_url='login')
def profile(request, username):
    user = User.objects.get(username=username)
    user_profile = userProfile.objects.get(user=user)
    if request.method == 'POST':
        user_profile.avatar = request.POST.get('img')
        user_profile.save()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)
@login_required(login_url='login')
def editprofile(request):
    user_profile = userProfile.objects.get(user=request.user)
    if request.method == 'POST' and 'text-data' in request.POST:
        user_profile.firstname = request.POST.get('firstname')
        user_profile.surname = request.POST.get('surname')
        user_profile.patronymic = request.POST.get('patronymic')
        user_profile.position = request.POST.get('position')
        user_profile.telegram = request.POST.get('telegram')
        user_profile.age = request.POST.get('age')
        user_profile.about = request.POST.get('about')
        user_profile.save()
        return redirect('index')
    elif request.method == 'POST' and 'image-data' in request.POST:
        image = request.FILES.get('avatar', False)
        if image:
            user_profile.avatar = image
        user_profile.save()
        return redirect('index')
    else:
        return render(request, 'main/editprofile.html', {'user_profile': user_profile})
# def editprofile(request):
#     return render(request, 'main/editprofile.html')
# def profile(request):
#     return render(request, 'main/profile.html')
# class Profile(TemplateView):
#     template_name = 'main/profile.html'
#
#     def get(self, request, login=None):
#         user = User.objects.get(username=login)
#         user_profile = userProfile.objects.get(user=user)
#         context = {"avatar": user_profile.avatar,
#                    "firstname": user_profile.firstname,
#                    "surname": user_profile.surname,
#                    "patronymic": user_profile.patronymic,
#                    "position": user_profile.position,
#                    "about": user_profile.about,
#                    }
#
#         return render(request, 'main/profile.html', context)



