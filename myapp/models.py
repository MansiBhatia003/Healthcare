from django.db import models

# Create your models here.
class userregister(models.Model):
    Firstname=models.CharField(max_length=100,blank=True,null=True)
    Lastname =models.CharField(max_length=100,blank=True,null=True)
    Username=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    CPassword=models.CharField(max_length=100)
    Address=models.CharField(max_length=1000,blank=True,null=True)
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.Username
