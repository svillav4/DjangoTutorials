from django.db import models 
from django.contrib.auth.models import User 


class ToDo(models.Model): 
    title = models.CharField(max_length=100) 
    memo = models.TextField(blank=True) 
 
    # Set to current time 
    created = models.DateTimeField(auto_now_add=True) 
    completed = models.BooleanField(default=False) 
 
    # User who posted 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
 
    def __str__(self): 
        return self.title
