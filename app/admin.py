from django.contrib import admin
from . models import Profile, Comment,Post,Follow
# Register your models here.
# my models
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Post)
