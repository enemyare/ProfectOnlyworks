from django.urls import path
from . import views # точка означает из этой же папки. Даём возможность обратится к виевс

urlpatterns = [
    path('', views.catalog, name='catalog'), #ссылаемся на метод в питонфайле индекс

]
