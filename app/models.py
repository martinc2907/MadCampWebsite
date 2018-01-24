from django.db import models
from django.contrib.auth.models import User


#The profile model implementation is wrong- should have those fields automatically filled in through Profile(request.post) in view. Not manually. 
#Change later
class Profile(models.Model):
	name = models.CharField(max_length = 50)
	school = models.CharField(max_length = 50)
	url = models.CharField(max_length = 1000)
	specialty = models.CharField(max_length = 500)
	github = models.CharField(max_length = 500)
	quote = models.CharField(max_length = 500)
	session = models.CharField(max_length = 20)

class Chat(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	message = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.message

class Board(models.Model):
	header = models.CharField(max_length = 100)
	content = models.CharField(max_length = 1000)
	file = models.ImageField(upload_to= 'images/')


