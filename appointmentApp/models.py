from django.db import models

# Create your models here.

class User(models.Model):
    Options = (
        ('morning', 'morning'),
        ('afternoon', 'afternoon'),
        ('evening', 'evening')
    )


    First_name= models.CharField( max_length=100)
    Last_name= models.CharField( max_length=100)
    email=models.EmailField( max_length=100)
    phone_number=models.CharField( max_length=20 )
    date=models.DateField( max_length=100)
    preference=models.CharField(max_length=10 , choices=Options)

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"