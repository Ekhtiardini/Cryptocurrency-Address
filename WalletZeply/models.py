from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    wallet_user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    wallet_name=models.CharField(max_length=255)
    wallet_des=models.TextField(null=True)
    wallet_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wallet_name
    
