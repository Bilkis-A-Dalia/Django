from django.db import models
from catagories.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    #one post can be in multiple category again in one catagory can have multiple categories  
    author = models.ForeignKey(User,on_delete=models.CASCADE) #all will be delete 

    def __str__(self):
        return self.title