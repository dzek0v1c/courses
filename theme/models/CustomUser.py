from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . CustomUserManager import CustomUserManager

class CustomUser (AbstractBaseUser,PermissionsMixin):
    first_name = models. CharField(max_length=50)
    last_name = models. CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    class Meta:
        permissions = (("can_view_custom_user", "Can view custom user"),)
        swappable = "AUTH_USER_MODEL"