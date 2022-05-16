from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


from department.models import Departments, Positions
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    
    date_of_birth = models.DateField(default=datetime.now)
    years_old = models.IntegerField(default=0)
    
    phone = PhoneNumberField(default="Phone number")
    login = models.CharField(max_length=30, default="login")
    email = models.EmailField(default="Mail address")
    
    pasportNum = models.CharField(max_length=15, default="Pasport num")
    pasportCode = models.CharField(max_length=15, default="Pasport code")
    pasportOtd = models.CharField(max_length=50, default="Pasport otd")
    pasportDate = models.CharField(max_length=15, default="Pasport date")
    
    inn_fiz = models.CharField(max_length=15, default="inn")
    oms = models.CharField(max_length=16, default="oms")
    
    address = models.CharField(max_length=50, default="Address")
    country = models.CharField(max_length=50, default="Country")
    region = models.CharField(max_length=50, default="Region")
    city = models.CharField(max_length=50, default="City")
    
    photo = models.ImageField(upload_to="personnel_photos")

    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, null=True, blank=True)
    if_dismissed = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile of the {self.user.username}"
