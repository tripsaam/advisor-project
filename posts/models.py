from django.db import models
from django.contrib.auth.models import User


class Advisor(models.Model):
    advisor_name = models.CharField(max_length=100)
    photo_url = models.URLField()
    # url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


# class Vote(models.Model):
#     voter = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)