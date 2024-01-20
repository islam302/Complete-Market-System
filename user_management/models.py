from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class UserModel(AbstractUser):

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    first_name = models.CharField(max_length=20, verbose_name='first_name')
    last_name = models.CharField(max_length=20, verbose_name='last_name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='gender')
    mobile_number = models.IntegerField(max_length=11, verbose_name='mobile_number')
    date_of_birth = models.DateField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = UserManager()
