from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def _str_(self):
        return self.name

class user_numbers(models.Model):
    user = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user

class plant(models.Model):
    title=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class cart_items(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey('Plant', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
