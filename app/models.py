from calendar import c
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

# class Image(models.Model):
#     name=models.TextField()
#     photo = CloudinaryField('image')
#     caption=models.CharField(max_length=300)
#     # author=models.ForeignKey(User,on_delete=models.CASCADE)
#     comment=models.TextField()

#     def __str__(self):
#         return self.name

#     # save
#     def save_photo(self):
#         self.save()
#     # delete
#     def delete_photo(self):
#         self.delete()

#     # update caption
#     @classmethod
#     def update_caption(cls,id,photo):
#         cls.object.filter(id=id).update(photo=photo)


class Post(models.Model):
    image = CloudinaryField('posts',null=True)
    caption = models.CharField(max_length=300,blank=True)
    date_posted = models.DateTimeField(default=now)
    name=models.CharField(max_length=100,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    dateTime = models.DateTimeField(default=now)
    location = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.image

# class PostImage(models.Model):
#     post= models.ForeignKey(Post, related_name="images" ,on_delete=models.CASCADE)
#     photo = CloudinaryField('image')

class Profile(models.Model):
    # author = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic',blank=True)
    bio=models.CharField(max_length=30)
    location = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200,blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments',null=True)
    # image=models.ForeignKey(Image, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(default=now)
    
    #
    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-pk']

class Follow(models.Model):
    followed = models.ForeignKey('Profile', on_delete=models.CASCADE)
    # follower = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} Follow'