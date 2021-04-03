from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option3 = models.CharField(max_length=100, blank = True)
    option1_count = models.IntegerField(default = 0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
