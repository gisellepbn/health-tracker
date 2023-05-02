from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'plans/index.html')


def sign_up(request):

    form = ProfileForm()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():

            profile = form.save(commit=False)
            profile.username = profile.username.lower()
            profile.save()

            login(request, profile)
            return redirect('account')
           
        else:
            messages.error(request, 'Try a different username.')
            return redirect('sign_up')
            

    return render(request, 'plans/sign-up.html', {
        'form': form
    })


@login_required
def account(request):
    return render(request, 'plans/account.html')


def log_out(request):
     logout(request)
     return redirect("index")