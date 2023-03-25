from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Each design should have the following properties: id, title, description, creator (user),
# price, creation date, last update date, and a list of tags.


class DesignModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    creator = models.CharField(max_length=50)
    price = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateField(auto_now=True)
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        ordering = ['title']