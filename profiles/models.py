from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


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
    email = models.EmailField(default="Mail address")
    photo = models.ImageField(upload_to="personnel_photos")

    def __str__(self):
        return f"Profile of the {self.user.username}"
