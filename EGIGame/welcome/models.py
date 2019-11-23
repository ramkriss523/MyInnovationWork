from django.db import models


# Create your models here.
class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    signum = models.CharField(max_length=10)


class QuestionData(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option5 = models.CharField(max_length=100)
    option6 = models.CharField(max_length=100)
