from django.db import models
from django.contrib.auth.models import User

# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    # string rep of class instance to get exact username on search
    # def __str__(self):
    #         return f'{self.user.username} Profile'

    def __str__(self):
        return self.user
    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

# class post
class Post(models.Model):
    image = models.ImageField(upload_to='posts/',null=True)
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts',null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #         return f'{self.user.username} Post'

    def __str__(self):
        return self.name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    

   
# add class comment
class Comment(models.Model):
    comment = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments',null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.objects.filter(post__pk=id).all()
        return comments

    



class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'

    def save_follow(self):
        self.save()

    def delete_follow(self):
        self.delete()

