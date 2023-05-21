from django.shortcuts import render
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
    return render(request, 'main/registration.html')
def sign(request):
    return render(request, 'main/sign.html')
def team(request):
    return render(request, 'main/team.html')