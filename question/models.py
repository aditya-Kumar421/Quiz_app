from django.db import models
from django.contrib.auth.models import User
# class Course(models.Model):
#     course_name = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.course_name
        
class Question(models.Model):
    # course = models.ForeignKey(Course, on_delete = models.CASCADE)
    question = models.CharField(max_length = 255)
    image_url = models.URLField(blank=True)
    answer = models.CharField(max_length = 100)
    option_one = models.CharField(max_length = 100, blank = True)
    option_two = models.CharField(max_length = 100, blank = True)
    option_three = models.CharField(max_length = 100, blank = True)
    option_four = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.question



#Score of Quiz:
class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # quiz_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s score is : {self.score}"
