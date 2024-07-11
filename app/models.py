from django.db import models

# Create your models here.

class Contact(models.Model):
        full_name = models.CharField(max_length=100)
        email = models.EmailField()
        phone_number = models.CharField(max_length=12)
        birth_date = models.DateField()
        gender = models.CharField(max_length=20)
        street_address = models.CharField(max_length=100)
        city = models.CharField(max_length=50)
        region = models.CharField(max_length=50)
        postal_code = models.CharField(max_length=10)
        country = models.CharField(max_length=50)