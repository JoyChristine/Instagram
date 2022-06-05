from django.contrib import admin
from django.urls import path


from . import views
from django.conf import settings
from django.conf.urls.static import static

import app


app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/',views.index,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('post/<id>', views.post_comment, name='comment'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)