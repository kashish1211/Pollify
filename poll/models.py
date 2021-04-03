from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option1_count = models.IntegerField(default = 0)
    option2_count = models.IntegerField(default=0)    
    votedBy = models.ManyToManyField(User, related_name = "votedBy", blank=True)
    percentage_o1 = models.FloatField(default = 0.0)
    percentage_o2 = models.FloatField(default = 0.0)
    image_bg = models.CharField(default="", max_length=100)
    

    def save(self):
    	super().save()
    

    def __str__(self):
    	return self.question


    	

	
