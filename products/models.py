from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    #id=models.AutoField()
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    content=models.TextField(null=True, blank=True)
    price=models.IntegerField(default=0)

    def __str__ (self):
        return self.title
        


