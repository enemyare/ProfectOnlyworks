from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField( upload_to="product_images", default='profile.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                               blank=True)
    firstname = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    patronymic = models.CharField(max_length=20, blank=False)
    position = models.CharField(max_length=1, blank=False)
    telegram = models.CharField(max_length=50, blank=False, default='@')
    age = models.CharField(max_length=3, blank=False)
    about = models.TextField(blank=False)
    def __str__(self):
        return self.user.username

class Myteam(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nameteam = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='product_images', default='profile.png', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], blank=True)
    player1 = models.CharField(max_length=50, blank=False, default="player",null=True)
    player2 = models.CharField(max_length=50, blank=False, default="player",null=True)
    player3 = models.CharField(max_length=50, blank=False, default="player",null=True)
    player4 = models.CharField(max_length=50, blank=False, default="player",null=True)
    player5 = models.CharField(max_length=50, blank=False, default="player",null=True)

    player1pos = models.CharField(max_length=1, blank=False, default='0',null=True)
    player2pos = models.CharField(max_length=1, blank=False, default='0',null=True)
    player3pos = models.CharField(max_length=1, blank=False, default='0',null=True)
    player4pos = models.CharField(max_length=1, blank=False, default='0',null=True)
    player5pos = models.CharField(max_length=1, blank=False, default='0',null=True)


    def __str__(self):
        return self.user.username

