from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User
from django.db import models
from quilljs.fields import RichTextField


class Credit(models.Model):
    user = AutoOneToOneField(User, related_name='credit', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)


class UserContactInfo(models.Model):
    user = AutoOneToOneField(User, related_name='contact_info', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, default='', blank=True, null=True)


class Offer(models.Model):
    price_in_points = models.IntegerField()
    title = models.CharField(max_length=200)
    description = RichTextField()
    cover_image = models.ImageField(null=True, blank=True)

    enabled = models.BooleanField(default=True, db_index=True)

    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserOfferApplication(models.Model):
    user = models.ForeignKey(User, related_name='offers', on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, related_name='user_offers', on_delete=models.CASCADE)

    redeem_time = models.DateTimeField(auto_now_add=True)

    permitted = models.BooleanField(default=False, db_index=True)
