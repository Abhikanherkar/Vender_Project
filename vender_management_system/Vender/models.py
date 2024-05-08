from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from Vender.custom_manager import CustomUserManager
from django.utils.translation import gettext_lazy as _


# class Account(AbstractUser):
class CustomUser(AbstractBaseUser, PermissionsMixin):
    UserTypeChoices = [
        ('Admin', "Admin"),
        ("Vender", "Vender")
    ]

    password = models.CharField(max_length=50)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False) 
    user_type = models.CharField(max_length = 50, null = False, choices = UserTypeChoices)
    

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Vender(models.Model):
    name = models.CharField(max_length = 50)
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, null=False, related_name = "vender_useraccount")
    contact_details = models.CharField(max_length = 50)
    address = models.TextField()
    vendor_code = models.CharField(max_length = 30, unique = True)
    on_time_delivery_rate = models.FloatField(default=0.)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
