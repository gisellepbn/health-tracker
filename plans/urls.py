from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('sign-up', views.sign_up, name='sign_up'),
 path('sign-in', views.sign_in, name='sign_in'),
 path('log-out', views.log_out, name='log_out'),
 path('plan', views.plan, name='plan'),
 path('plan/<str:plan>/<str:date>', views.plan, name='plan'),
 path('plan/progress/<str:date>/<uuid:id>', views.plan_id, name='plan_id'),
]