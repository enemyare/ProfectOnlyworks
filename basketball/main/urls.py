from django.urls import path
from . import views # точка означает из этой же папки. Даём возможность обратится к виевс

urlpatterns = [
    path('', views.index), #ссылаемся на метод в питонфайле индекс
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('sign/', views.sign, name='sign'),
    path('team/', views.team, name='team'),

]
