from django.db import models
from datetime import date
from django_countries.fields import CountryField

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    
    '''Model definition for ModelName.'''
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50,verbose_name='Фамилия')
    email = models.EmailField(unique=True,verbose_name='Электронная почта')
    birth_date = models.DateField(default=date(2000, 1, 1), verbose_name='Дата рождения')
    profile_image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография профиля')
    country = CountryField(blank_label="(select country)", blank=True, verbose_name='Страна')
    is_superuser = models.BooleanField(default=False,verbose_name='Суперюзер?')
    is_staff = models.BooleanField(default=False,verbose_name='Стафф?')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        '''Meta definition for ModelName.'''

        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.first_name
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, myPage):
        return self.is_superuser
    

    

class PostModel(models.Model):
    '''Model definition for ModelName.'''
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        '''Meta definition for ModelName.'''

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
    
