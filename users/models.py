from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string


class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=False, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    bio = models.TextField(max_length=1024)
    code = models.CharField(max_length=24, blank=True)
    phone_number = models.IntegerField(_('phone number'), blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{super().first_name} {super().last_name}'

    def set_code(self):
        code = get_random_string(24)
        self.code = code
        self.save()
        return code
