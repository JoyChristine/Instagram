
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from django.forms import modelformset_factory
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'registration/registration_form.html')

    
@login_required
def home(request):
    return render(request, 'home.html')

