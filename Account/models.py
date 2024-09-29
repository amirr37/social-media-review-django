from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Relation(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')

    def __str__(self):
        return f" {self.follower} follows {self.following}"


