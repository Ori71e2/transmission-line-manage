# Create your models here.
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


class User(AbstractBaseUser):   # 定义自己的用户表
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=100, verbose_name='用户名')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    #is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = '用户详细信息'
        db_table = 'user'
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.email

    def get_short_name(self):
        """Return the short name for the user."""
        return self.email
        
    def __str__(self):
        return self.email
      

class UserSalt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    salt = models.CharField(max_length=10, verbose_name='加密用盐值')
    user_id = models.UUIDField(default=None, null=True, blank=True, verbose_name='用户信息表', unique=True)

    class Meta:
        verbose_name = '加密用盐值'
        db_table = 'user_salt'

        
    def __str__(self):
        return self.salt