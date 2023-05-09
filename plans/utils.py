from .models import Plan
from datetime import datetime, timedelta


def plans_per_date(request, date):

    nutrition_plan = Plan.objects.filter(profile=request.user, date=date, category='Nutrition')
    water_plan = Plan.objects.filter(profile=request.user, date=date, category='Water_Intake')
    exercise_plan = Plan.objects.filter(profile=request.user, date=date, category='Exercise')
    sleep_plan = Plan.objects.filter(profile=request.user, date=date, category='Sleep')

    return nutrition_plan, water_plan, exercise_plan, sleep_plan


def plans_per_category_per_date(request, category, date):
    return Plan.objects.filter(profile=request.user, date=date, category=category)



def percentage_per_category(plans_per_category_per_date):

    # General percentage of goal reached for that category on that date
    percentage = 0;

    for plan in plans_per_category_per_date:
        percentage += ((100/plans_per_category_per_date.count())*plan.progress)/plan.goal 
    
    return percentage


def weekly_progress(request, category, base_date):

    # Convert str with date taken from selected date
    end_date = datetime.strptime(base_date, '%Y-%m-%d')    
    date_list = [end_date - timedelta(days=x) for x in reversed(range(7))]
 
    list_percentages = []

    for date in date_list:
        plans = plans_per_category_per_date(request, category, date)
        percentage = percentage_per_category(plans)
        list_percentages.append(
            {
                'date': date.strftime('%b %d, %Y'),
                'percentage':percentage
            }
            )
  
    return list_percentages