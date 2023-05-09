from django.urls import path
from . import views # точка означает из этой же папки. Даём возможность обратится к виевс

urlpatterns = [
    path('', views.index, name='home'), #ссылаемся на метод в питонфайле индекс
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]
