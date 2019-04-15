from django.db import models

# Create your models here.
class BinRecord(models.Model):
    bin_number = models.IntegerField(primary_key='True')
    saved_number = models.IntegerField()
    last_number = models.TextField()
    second_last_number =  models.TextField()




