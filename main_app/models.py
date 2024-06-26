from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code + ' - ' + self.name
    
    