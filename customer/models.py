from django.db import models
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField(max_length=15)
    customer_phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    customer_address = models.TextField(max_length=50)