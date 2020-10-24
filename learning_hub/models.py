from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager
from django.db import models, IntegrityError
from django.db.utils import DataError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import PermissionsMixin


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ['email'] #A list of the field names that will be prompted for when creating a user via the createsuperuser management command
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Users'


    @staticmethod
    def create(email, username, password):
        user = Users(email = email, username = username, password = password)
        user.set_password(password)
        try:
            validate_email(user.email)
            user.save()
            return user
        except (IntegrityError, AttributeError, ValidationError, DataError):
            pass
        
        
class Questions(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
        
        
    class Meta:
        verbose_name_plural = 'Questions'
        
        
'''
# Create your models here.
class Category(models.Model):
    categ_name = models.CharField(max_length = 50, unique = True)
    
    
class Meta:
    verbose_name_plural = 'Categories'
    
    
class Resource(models.Model):
    categ_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length = 50, unique = True)
    resource_desc = models.TextField(blank = True, max_length = 300)
    
    
class Meta:
    verbose_name_plural = 'Resources'
'''