from django.db import models
from authentication.models import User
import datetime
# Create your models here.
class Order(models.Model):
    item = models.CharField(max_length=50)    
    amount = models.DecimalField(max_digits=10,decimal_places=2)  
    customer = models.ForeignKey(to = User, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering: ['-created']
    
    def __str__(self):
        return self.item