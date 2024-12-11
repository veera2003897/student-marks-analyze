from django.db import models

# Create your models here.
class marks2(models.Model):
    rono=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=120)
    sub1=models.FloatField()
    sub2=models.FloatField()
