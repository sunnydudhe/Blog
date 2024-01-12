from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User






class categories(models.Model):
    cate=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.cate

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100,null=True,blank=True)
    content=RichTextField()
    image=models.ImageField(upload_to='post_media',null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    category=models.ForeignKey(categories,on_delete= models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='post_media', blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.user.username
    
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    blog_post = models.ForeignKey(post, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.blog_post.title
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


   


    









