from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class food(models.Model):
    title = models.CharField(max_length = 50)
    descriptions = models.TextField()
    photo = models.ImageField(upload_to="food")
    update_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)






    


