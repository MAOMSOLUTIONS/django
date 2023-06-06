from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    last_login = models.DateTimeField()
    groups = models.ManyToManyField(
        Group, related_name='auth_users', related_query_name='auth_user_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name='auth_users', related_query_name='auth_user_set', blank=True
    )


class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    owners = models.ManyToManyField(
        User, related_query_name='pet_pets', related_name='pet_set'
    )
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    breed = models.CharField(max_length=100)
    deceased_date = models.DateField(blank=True, null=True)
