# import email
from django.db import models
from django.forms import CharField, FileField

from django.core.validators import RegexValidator

# Create your models here.
class Driver_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, unique=True) # Validators should be a list
    # phone_number = models.IntegerField(unique=True)
    # phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    vehicle_registration_number = models.CharField(max_length=50,unique=True)
    driving_licence_number = models.CharField(max_length=50,unique=True)
    registration_card_photo = models.FileField(blank=True,null=True)
    driving_licence_photo = models.FileField(blank=True,null=True)
    # vehicle_registration_number = models.ImageField(upload_to='images/')
    # driving_licence_number = models.ImageField(upload_to='images/')


    



    
    