from django.db import models
from djang.contrib.auth.models import User
# Create your models here.

class MyUser(User):
	name = models.CharField('First name', max_length=50, blank=True, null=True)
	username = models.CharField('Username', max_length=50, unique=True)
	password1 = models.CharField('Passowrd 1', max_length=50)
	password2 = models.CharField('Passowrd 2', max_length=50)