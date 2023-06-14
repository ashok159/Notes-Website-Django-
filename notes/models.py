from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #create foreign key between Notes table and User table w/ built in User function
    #passes the related table, what happens when a user is deleted, and the related name b/w tables
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")