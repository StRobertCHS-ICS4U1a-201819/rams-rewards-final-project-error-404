from django.db import models

class Reward(models.Model):
    reward_title = models.CharField(max_length=200)
    reward_description = models.CharField(max_length=500)
    point_value = models.IntegerField(default=0)
    
    def __str__(self):
        return self.reward_title
