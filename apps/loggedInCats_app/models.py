from __future__ import unicode_literals

from django.db import models
from ..cats_app.models import User


# Create your models here.
class CatManager(models.Manager):
    def addNewCat(self, postData, id):
        if not postData['name'] or not postData['age']:
            return
        user = User.objects.get(id=id)
        Cat.objects.create(name=postData['name'], age=postData['age'], likes=0, user=user)
        return user

class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    likes = models.IntegerField()
    user = models.ForeignKey(User)
    objects = CatManager()

