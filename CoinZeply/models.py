from django.db import models
from django.contrib.auth.models import User

class Coin(models.Model):
    coin_author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    coin_name=models.CharField(max_length=255)
    coin_sign=models.CharField(max_length=8)
    concoin_des = models.TextField(null=True)

    def __str__(self):
        return self.coin_name

# Create your models here.
