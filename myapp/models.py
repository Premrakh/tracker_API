from typing import Iterable, Optional
from django.db import models
import socket

# Create your models here.


# def get_ip_address():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return ip_address



class ScreenShot(models.Model):
    IP=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.IP

class User(models.Model):
    username=models.CharField(max_length=100,unique=True,default=None,null=True,blank=True)                                                                                                                                                                                                 
    IP=models.CharField(max_length=70)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)
    ss_count=models.IntegerField(default=3,null=True,blank=True)
    time_gap=models.IntegerField(default=10,null=True,blank=True)

    def __str__(self):
        return self.IP