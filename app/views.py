from genericpath import exists
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm, UpdateUserProfileForm, PostForm, CommentForm
from django.contrib.auth import login, authenticate
from .models import Post, Comment, Profile, Follow
from django.contrib.auth.models import User
from django.template.loader import render_to_string

# sign up function 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=name, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required(login_url='login')
def index(request):
    # see posts & users
    images = Post.objects.all()
    users = User.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    return render(request, 'app/index.html', {'images': images, 'form': form, 'users': users})


@login_required
def profile(request, username):
    Profile.objects.get_or_create(user=request.user)
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        updateUserProfileForm = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if updateUserProfileForm.is_valid():
            updateUserProfileForm.save()
        return HttpResponseRedirect(request.path_info)
    else:
       
        updateUserProfileForm = UpdateUserProfileForm(instance=request.user.profile)
    return render(request, 'app/user.html', {'UpdateUserProfileForm': UpdateUserProfileForm, 'images': images, 'updateUserProfileForm': updateUserProfileForm})



@login_required(login_url='login')
def user_profile(request, username):
    # Calls get() on profile model, but it raises Http404 instead of the model’s DoesNotExist exception.
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    # helps add and remove followers
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False

    context ={
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
         }
    
    return render(request, 'app/profile.html', context)



@login_required(login_url='login')
def comment(request, id):
    image = get_object_or_404(Post, pk=id)
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {
        'image': image,
        'form': form,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    return render(request, 'app/comment.html', context)


@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        context = {'results': results,'message': message }
        return render(request, 'app/results.html', context)
    else:
        message = "Try again"
    return render(request, 'app/results.html', {'message': message})


def like(request,id):
    image = Post.objects.get(pk=id)
    # image = get_object_or_404(Post, id=request.GET.get('id'))
    is_liked = False
    user = request.user.profile

    try:
        profile = Profile.objects.get(user=user.user)

    except Profile.DoesNotExist:
        raise Http404()


    # total_likes = image.total_likes()
    if image.likes.filter(id=user.user.id).exists():
        image.likes.remove(user.user)
        is_liked=False

    else:
        image.likes.add(user.user)
        is_liked = True


    return HttpResponseRedirect(reverse('index'))


def follow(request, id):
    if request.method == 'GET':
        followed = Profile.objects.get(pk=id)
        follow_s = Follow(follower=request.user.profile, followed= followed)
        follow_s.save()
        return redirect('user_profile',  followed.user.username)

def unfollow(request, id):
    if request.method == 'GET':
        unfollow = Profile.objects.get(pk=id)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=unfollow)
        unfollow_d.delete()
        return redirect('user_profile',  unfollow.user.username)
