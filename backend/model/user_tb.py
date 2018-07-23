# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import uuid

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email :
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):   # 定义自己的用户表
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=100, verbose_name='用户名', unique=True)
    is_active = models.BooleanField(default=True)
    #is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return str(self.email)

    def get_short_name(self):
        """Return the short name for the user."""
        return str(self.email)
        
    def __str__(self):
        return str(self.email)
      



