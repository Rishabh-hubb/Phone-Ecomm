from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import random


#creating abstractuser to add phone_number to model
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)


#model to generate otp
class Code(models.Model):
    otp = models.CharField(max_length=4)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.otp)

    def save(self,*args,**kwargs):
        self.otp = str(random.randint(1000,9999))
        super().save(*args,**kwargs)


#Models for phones
class PhoneModel(models.Model):
    title = models.CharField(max_length = 70)
    color = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    specification = models.TextField()
    image = models.ImageField(default='no_image.png',upload_to='model-image')
