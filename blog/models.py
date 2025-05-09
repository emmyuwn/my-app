from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    description = models.TextField()

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
    from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dashboard_type = models.CharField(max_length=20, choices=[("dash1", "Dashboard 1"), ("dash2", "Dashboard 2"), ("dash3", "Dashboard 3")])





