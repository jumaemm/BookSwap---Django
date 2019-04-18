from django.db import models
from django.contrib import auth
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):
    phone_num = models.IntegerField(unique = True)
    def __str__(self):
        return "{}".format(self.username)
