from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Visitor(AbstractUser):
    profile = models.ImageField(upload_to='profile_pics', null=True)

    def __unicode__(self):
        return self.username


class Feed(models.Model):
    feed_url = models.URLField()
    visitor = models.ForeignKey(Visitor, related_name='feeds')

    def __unicode__(self):
        return self.feed_url

class Category(models.Model):
    name = models. CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Visitor, related_name='categories')

    def __unicode__(self):
        return self.name