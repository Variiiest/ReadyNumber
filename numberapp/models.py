from django.db import models

class Numbers(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    answer= models.IntegerField()
    
