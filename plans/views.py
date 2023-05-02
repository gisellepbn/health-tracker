from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

# Create your views here.

def index(request):
    return render(request, 'plans/index.html')


def sign_up(request):

    form = ProfileForm()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():


            name = request.POST['name'].lower()
            username = request.POST['username'].lower()
            password = request.POST['password']
            picture = request.POST['profile_picture']

            profile = Profile.objects.create_user(name=name, username=username, password=password, profile_picture = picture)
            profile.save()

            login(request, profile)
            return redirect('account')
           
        else:
            messages.error(request, 'Try a different username.')
            return redirect('sign_up')
            

    return render(request, 'plans/sign-up.html', {
        'form': form
    })


def sign_in(request):

    if request.user.is_authenticated:
        redirect('account')

    form = ProfileForm()

    if request.method == 'POST':        

        username = request.POST['username'].lower()
        password = request.POST['password']

        profile = authenticate(request, username=username, password=password)
          
        if profile is not None:
            login(request, profile)
            return redirect('account')
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('sign_in')
          
    
    else:
         return render(request, 'plans/sign-in.html', {
             'form': form
         }) 



@login_required
def account(request):
    return render(request, 'plans/account.html')

@login_required
def log_out(request):
     logout(request)
     return redirect("index")