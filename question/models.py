from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length = 500, unique = True)
    image_url = models.URLField(blank=True)
    answer = models.CharField(max_length = 500)
    option_one = models.CharField(max_length = 500,blank=True)
    option_two = models.CharField(max_length = 500,blank=True)
    option_three = models.CharField(max_length = 500,blank=True)
    option_four = models.CharField(max_length = 500,blank=True)

    def __str__(self):
        return self.question


class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s score is : {self.score}"

    