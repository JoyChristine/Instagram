from calendar import c
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Image(models.Model):
    name=models.TextField()
    photo = CloudinaryField('image')
    caption=models.CharField(max_length=300)
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self):
        return self.name

    # save
    def save_photo(self):
        self.save()
    # delete
    def delete(self):
        self.delete()

    # update caption
    @classmethod
    def update_caption(cls,id,photo):
        cls.object.filter(id=id).update(photo=photo)









class Profile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic',blank=True)
    bio=models.CharField(max_length=30)

    def __str__(self):
        return self.name

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField(max_length=200,blank=True)
#     image=models.ForeignKey(Image, on_delete=models.CASCADE)
#     parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
#     dateTime = models.DateTimeField(default=now)
    
#     #
#     def __str__(self):
#         return self.content
