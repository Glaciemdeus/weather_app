from django.db import models







class UserRequestModel(models.Model):
    
    city = models.CharField(max_length=50)
    temperature = models.IntegerField()
    
    
    
