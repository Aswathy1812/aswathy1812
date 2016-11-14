from __future__ import unicode_literals
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

from django.db import models

# Create your models here.

class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None):
        user = self.user(username=username)
        user.set_password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user
        user.is_admin = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    first_name = models.CharField(null=True, blank=True, max_length=128)
    last_name = models.CharField(null=True, blank=True,  max_length=128)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=25)  # validators should be a list
    username = models.CharField(blank=False, unique=True, max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    object = AppUserManager()

    USERNAME_FIELD = 'username'

