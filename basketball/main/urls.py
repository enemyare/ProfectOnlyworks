from django.urls import path
from . import views # точка означает из этой же папки. Даём возможность обратится к виевс

urlpatterns = [
    path('', views.index, name='index'), #ссылаемся на метод в питонфайле индекс
    path('profile/<str:username>', views.profile, name='profile'),
    path('registration/', views.RegiserView.as_view(), name='registration'),
    path('sign/', views.sign, name='sign'),
    path('team/', views.team, name='team'),
    path('myteam/<str:username>', views.myteam, name='myteam'),
    path('logout/', views.logout, name='logout'),
    path('editprofile/ ', views.editprofile, name='editprofile'),
    path('editmyteam/ ', views.editmyteam, name='editmyteam'),

]
