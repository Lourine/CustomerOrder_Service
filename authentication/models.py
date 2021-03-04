from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,PermissionsMixin)

class UserManager(BaseUserManager):
    
    def create_user(self,username,email,password:None, phone_number):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have an Email')
        if phone_number is None:
            raise TypeError('Users should have a Phone Number')

        user= self.model(username=username, email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,email,phone_number,password:None):
        if password is None:
            raise TypeError('Password should not be None')

        user= self.create_user(username,email,password,phone_number)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}
                  
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    phone_number=models.CharField(max_length=13)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','phone_number']

    objects = UserManager()
    def __str__(self):
        return self.email
        
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    