from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

# sign up form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Please input your email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ('profile_picture', 'bio')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Comment
        fields = ('comment',)
