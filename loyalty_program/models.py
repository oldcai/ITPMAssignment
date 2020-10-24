from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models


class Credit(models.Model):
    user = AutoOneToOneField(User, related_name='credit', on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)
