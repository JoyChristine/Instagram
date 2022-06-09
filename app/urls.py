from django.urls import path, include

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<id>/', views.comment, name='comment'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('search/', views.search_profile, name='search'),
    path('like/<id>', views.like, name='like'),
    path('unfollow/<id>', views.unfollow, name='unfollow'),
    path('follow/<id>', views.follow, name='follow')
]
