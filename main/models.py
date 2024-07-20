from django.db import models







class UserRequestModel(models.Model):
    
    city = models.CharField(max_length=50)
    current_temperature = models.IntegerField()
    time = models.CharField(max_length=50)
    
    
    
