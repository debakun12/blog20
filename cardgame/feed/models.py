from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# add author name, date,  to models


class feedtable(models.Model):
    nameoftable = models.CharField(max_length=200)

    def __str__(self):
        return self.nameoftable


class feed(models.Model):
    feed_table = models.ForeignKey(feedtable, on_delete=models.CASCADE)
    display_title = models.CharField(max_length=200)
    display_text = models.CharField(max_length=200)
    content_blog = models.CharField(max_length=1000)
    display_link = models.CharField(max_length=200)
    display_photo = models.CharField(max_length=200)

    def __str__(self):
        return self.display_title
