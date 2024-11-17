from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Jewels(models.Model):
    jewels_id=models.TextField()
    category=models.TextField()
    jewels_name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    description=models.TextField()
    img=models.FileField()
    
    def __str__(self):
        return self.jewels_name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    product=models.ForeignKey(Jewels,on_delete=models.CASCADE)

class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Jewels,on_delete=models.CASCADE)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)  

class Jewels_category(models.Model):
    jewels_id=models.TextField()
    category=models.TextField()
    jewels_name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    description=models.TextField()
    img=models.FileField()
    Golden=models.BooleanField(default=False)
    Diamond=models.BooleanField(default=False)
     
  
    