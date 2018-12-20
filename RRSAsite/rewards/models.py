from django.db import models
from django.contrib.auth.models import AbstractUser

class Reward(models.Model):
    reward_title = models.CharField(max_length=200)
    reward_description = models.CharField(max_length=500)
    point_value = models.IntegerField(default=0)
    
    def __str__(self):
        return self.reward_title


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    