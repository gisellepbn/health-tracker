from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Plan
from .utils import plans_per_date, percentage_per_category, weekly_progress
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
import os
from datetime import date
from django.http import JsonResponse
import json



def index(request):
    return render(request, 'plans/index.html')


def sign_up(request):

    form = ProfileForm()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():

            try:
                profile = form.save(commit=False)
                profile.username = profile.username.lower()
                profile.password = make_password(profile.password)
                profile.save()  

                login(request, profile)
                return redirect('plan', 'goals', date.today())
            except IntegrityError:
                messages.error(request, 'Try a different username.')
                return redirect('sign_up') 
         
            

    return render(request, 'plans/sign-up.html', {
        'form': form
    })


def sign_in(request):

    if request.user.is_authenticated:
        redirect('plan', 'goals', date.today())

    form = ProfileForm()

    if request.method == 'POST':        

        username = request.POST['username'].lower()
        password = request.POST['password']

        profile = authenticate(request, username=username, password=password)
          
        if profile is not None:
            login(request, profile)
            return redirect('plan','goals', date.today())
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('sign_in')
          
    
    else:
         return render(request, 'plans/sign-in.html', {
             'form': form
         }) 



@login_required(login_url='sign_in')
def log_out(request):
     logout(request)
     return redirect("index")


@login_required(login_url='sign_in')
def plan(request, label, date=date.today()):

   
    nutrition_plan, water_plan, exercise_plan, sleep_plan = plans_per_date(request, date)

    nutrition_percentage = percentage_per_category(nutrition_plan)
    water_intake_percentage = percentage_per_category(water_plan)
    exercise_percentage = percentage_per_category(exercise_plan)
    sleep_percentage = percentage_per_category(sleep_plan)

    nutrition_weekly = weekly_progress(request, 'Nutrition', date)
    water_weekly = weekly_progress(request, 'Water_Intake', date)
    exercise_weekly = weekly_progress(request, 'Exercise', date)
    sleep_weekly = weekly_progress(request, 'Sleep', date)


    return render(request, 'plans/plan.html', {
        'nutrition_plan': nutrition_plan,
        'water_plan': water_plan,
        'exercise_plan': exercise_plan,
        'sleep_plan': sleep_plan,
        'date': date,
        'label': label,
        'nutrition_percentage': nutrition_percentage,
        'water_intake_percentage': water_intake_percentage,
        'exercise_percentage': exercise_percentage,
        'sleep_percentage': sleep_percentage,
        'nutrition_weekly': nutrition_weekly,
        'water_weekly': water_weekly,
        'exercise_weekly': exercise_weekly,
        'sleep_weekly': sleep_weekly
    })



@login_required(login_url='sign_in')
def plan_id(request, date, id):

    if request.method == "GET":
        try:
            plan = Plan.objects.get(id = id)     
        except Plan.DoesNotExist:
            return JsonResponse({"error": "Plan not found."}, status=404)
  
        return JsonResponse(plan.serialize())

    
@login_required(login_url='sign_in')
def edit_profile(request):

    profile = request.user

    form = ProfileForm(instance=profile)

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if 'update' in request.POST and form.is_valid():
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.password = make_password(user.password)
            user.save()

            login(request, user)
            return redirect('plan', 'goals', date.today())
            
            
        else:
            messages.error(request, 'Information is not valid')



    return render(request, 'plans/edit-profile.html', {
        'form': form
    })


@login_required(login_url='sign_in')
def cancel(request):
    return redirect('plan','goals', date.today())