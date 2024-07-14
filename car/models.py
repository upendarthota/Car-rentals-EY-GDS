from django.db import models
from datetime import datetime

class Car(models.Model):
    car_id = models.AutoField(primary_key=True,default=0)
    car_name=models.CharField(max_length=30,default="")
    car_desc=models.CharField(max_length=300,default="")
    posted=models.DateField(default=datetime.now,blank=True)
    car_seater=models.IntegerField(default=0)
    car_fuel=models.CharField(max_length=10,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="carimg/images",default="")
    
    def __str__(self):
        return self.car_name
    
class Meta:
    verbose_name='Car'
    verbose_name_plural='Cars'
    
    
class Rent(models.Model) :
    
    oid = models.AutoField(primary_key=True)  # Add primary_key=True to keep oid as the primary key
    # userid = models.IntegerField(default=0)
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    car_name= models.CharField(max_length=50,default="")
    car_seater = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    car_fuel = models.CharField(max_length=50,default="")
    days_for_rent = models.IntegerField(default=0)
    fromdate = models.DateField(default=datetime.now,blank=True)
    todate=models.DateField(default=datetime.now,blank=True)
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")
    totalbill=models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key=True,default=0)

    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name
    
class Payment(models.Model):
    cardno=models.CharField(max_length=20,default="")
    expdate=models.DateField(default=datetime.now,blank=True)
    cvv=models.IntegerField(default=0)
    cardholder=models.CharField(max_length=50,default="")
    amount=models.CharField(max_length=50,default="")
    
    
    
    def __str__(self):
        return self.name