from django.db import models

# Create your models here.
class userProfile(models.Model):
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/")
    login = models.CharField(max_length=50, blank=False)
    firstName = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    patronymic = models.CharField(max_length=20, blank=False)
    position = models.CharField(max_length=50, blank=False)
    about = models.TextField(blank=False)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'