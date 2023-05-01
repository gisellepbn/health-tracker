from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('sign-up', views.sign_up, name='sign_up'),
 path('account', views.account, name='account'),
 path('log-out', views.log_out, name='log_out'),

]