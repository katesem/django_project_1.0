from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager


ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)

class Users(AbstractBaseUser):
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    password = models.CharField(max_length=128)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)
    

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()
    
    REQUIRED_FIELDS = ['email'] #A list of the field names that will be prompted for when creating a user via the createsuperuser management command
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = 'Users'
        
        
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