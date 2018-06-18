"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将新建的app放在backend中，这里设置app搜索路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 添加模块搜索路径
sys.path.append(os.path.join(BASE_DIR, 'apps/common_modules'))
sys.path.append(os.path.join(BASE_DIR, 'backend'))
sys.path.append(os.path.join(BASE_DIR, 'backend/modules'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9q#d(^(u0lc1w9)1*g*+^wthv+d$70v6z_jrhv-ik&315g$h7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 使用自定义的管理页面
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'backend',   # 新建App 
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#ROOT_URLCONF = 'website.urls'
# 重新设置 ROOT_URLCONF 为一级，为了我们自己的定制
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['frontend/dist'],      # index.html搜索路径配置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Add for vuejs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/dist/static"),     # 静态文件搜索路径设置
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# 设置数据库为MySql数据库
# 配置写在一个json文件中， 注意文件路径
DATABASE_ENGINE = 'django.db.backends.mysql'

MYSQL_SETITNG =  json.load(open(BASE_DIR+"/website/mysql.json", encoding='utf-8'))
MYSQL_DATABASE = MYSQL_SETITNG['database']
MYSQL_USER = MYSQL_SETITNG['user']
MYSQL_PASSWORD = MYSQL_SETITNG['password']
MYSQL_HOST = MYSQL_SETITNG['host']
MYSQL_PORT = MYSQL_SETITNG['port']

# 连接后设置数据编码
INIT_COMMAND =  'set character_set_client = utf8mb4,' \
                'character_set_server = utf8mb4,' \
                'character_set_connection = utf8mb4,' \
                'character_set_database = utf8mb4,' \
                'character_set_results = utf8mb4,' \
                'collation_connection = utf8mb4_general_ci,' \
                'collation_database = utf8mb4_general_ci,' \
                'collation_server = utf8mb4_general_ci;'

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': MYSQL_DATABASE,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASSWORD,
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
        'OPTIONS': {
            #'init_command': INIT_COMMAND
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
