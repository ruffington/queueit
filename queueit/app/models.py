from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

class Organization(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	owner = models.CharField(max_length=100)
	members = models.ManyToManyField(User)
