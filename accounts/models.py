from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, blank=True)
    postal_code = models.CharField(max_length=20, verbose_name='почтовый индекс', blank=True)
    city = models.CharField(max_length=100, verbose_name='город', blank=True)
    street = models.CharField(max_length=100, verbose_name='улица', blank=True)
    house = models.CharField(max_length=100, verbose_name='дом', blank=True)
    building = models.CharField(max_length=100, verbose_name='корпус', blank=True)
    apartment = models.CharField(max_length=100, verbose_name='квартира', blank=True)

    def __str__(self):
        return self.user.first_name
