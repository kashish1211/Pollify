from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option3 = models.CharField(max_length=100, blank = True)
    option1_count = models.IntegerField(default = 0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
    back_image = models.ImageField(default = 'default.jpg',upload_to='background_pics')
    votedBy = models.ManyToManyField(User, related_name = "votedBy", blank=True)

    def save(self):
    	super().save()
    	img = Image.open(self.back_image.path)
    	if img.height>300 or img.width > 300:
    		output_size=(300,300)
    		img.thumbnail(output_size)
    		img.save(self.back_image.path)

    def __str__(self):
    	return self.question


    	

	
