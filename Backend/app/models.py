from django.db import models
from django.contrib.auth.models import User
import time
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.




class Society(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name + self.sector



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    society = models.ForeignKey(Society,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/",null=True,blank=True)
    phone = models.CharField(max_length=13)
    alternative_phone = models.CharField(max_length=13,null=True,blank=True)
    tower_number = models.CharField(max_length=100)
    flat_no = models.CharField(max_length=100)
    is_varified = models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.user.username)


class Category(models.Model):
    name = models.CharField(max_length=100)
    # shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class Shop(models.Model):
    society = models.ForeignKey(Society,name='society',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,name="category",on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    s_type = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True,null=True)
    items = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name + self.number    

class Product(models.Model):
    user = models.ForeignKey(User,name='user',on_delete=models.CASCADE)
    society = models.ForeignKey(Society,name='society',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)
    purchase_year = models.IntegerField(blank=True,null=True)
    model = models.CharField(max_length=100,blank=True,null=True)
    is_activated = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    is_negotiable = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name + self.user.username


