from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models


class Credit(models.Model):
    user = AutoOneToOneField(User, related_name='credit', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


class UserContactInfo(models.Model):
    user = AutoOneToOneField(User, related_name='contact_info', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, default='', blank=True, null=True)

