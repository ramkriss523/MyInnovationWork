from django.db import models


# Create your models here.
class UserData(models.Model):
    fullname = models.CharField(max_length=50)
    signum = models.CharField(max_length=10, primary_key=True)
    achiever = models.CharField(max_length=100, default="")
    philanthropist = models.CharField(max_length=100, default="")
    disruptor = models.CharField(max_length=100, default="")
    socializer = models.CharField(max_length=100, default="")
    player = models.CharField(max_length=100, default="")
    freespirit = models.CharField(max_length=100, default="")


class QuestionData(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option5 = models.CharField(max_length=100)
    option6 = models.CharField(max_length=100)
    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')
    image3 = models.ImageField(null=True, blank=True, upload_to='images/')
    image4 = models.ImageField(null=True, blank=True, upload_to='images/')
    image5 = models.ImageField(null=True, blank=True, upload_to='images/')
    image6 = models.ImageField(null=True, blank=True, upload_to='images/')
