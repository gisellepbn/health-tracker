from .models import Plan

def plans_per_date(request, date):

    nutrition_plan = Plan.objects.filter(profile=request.user, date=date, category='Nutrition')
    water_plan = Plan.objects.filter(profile=request.user, date=date, category='Water_Intake')
    exercise_plan = Plan.objects.filter(profile=request.user, date=date, category='Exercise')
    sleep_plan = Plan.objects.filter(profile=request.user, date=date, category='Sleep')

    return nutrition_plan, water_plan, exercise_plan, sleep_plan


def percentage_per_category(plans_per_category_per_date):

    # General percentage of goal reached for that category on that date
    percentage = 0;

    for plan in plans_per_category_per_date:
        percentage += ((100/plans_per_category_per_date.count())*plan.progress)/plan.goal 
    
    return percentage

