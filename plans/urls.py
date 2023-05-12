from django.urls import path
from . import views



urlpatterns = [
 path('', views.index, name='index'),
 path('sign-up', views.sign_up, name='sign_up'),
 path('sign-in', views.sign_in, name='sign_in'),
 path('log-out', views.log_out, name='log_out'),
 path('plan', views.plan, name='plan'),
 path('plan/<str:label>/<str:date>', views.plan, name='plan'),
 path('plan/progress/<str:date>/<uuid:id>', views.plan_id, name='plan_id'),
 path('profile', views.edit_profile, name='edit_profile'),
 path('cancel', views.cancel, name='cancel'),
 path('cancel/<str:label>/<str:date>', views.cancel, name='cancel'),
 path('delete-profile', views.delete_profile, name='delete_profile'),
 path('edit-goal/<uuid:plan_id>', views.edit_goal, name='edit_goal'),
 path('delete-plan/<uuid:plan_id>', views.delete_plan, name='delete_plan'),
 path('edit-progress]/<uuid:plan_id>', views.edit_progress, name='edit_progress'),
 path('add-plan/<str:category>/<str:date>', views.add_plan, name='add_plan'), 
]