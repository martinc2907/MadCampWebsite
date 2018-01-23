from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length = 50)
	school = models.CharField(max_length = 50)
	url = models.CharField(max_length = 1000)
	specialty = models.CharField(max_length = 500)
	github = models.CharField(max_length = 500)
	quote = models.CharField(max_length = 500)
	session = models.CharField(max_length = 20)