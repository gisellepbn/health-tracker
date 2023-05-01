from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(null=True, upload_to='profile/')

    class Meta:
        ordering = ['name']

    
    def __str__(self):
        return self.username


class Plan(models.Model):

    CATEGORIES = [
         ('Nutrition', 'Nutrition'),
         ('Water_Intake', 'Water Intake'),
         ('Exercise', 'Exercise'),
         ('Sleep', 'Sleep')
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    parameter = models.CharField(max_length=200)
    goal = models.FloatField()
    progress = models.FloatField()
    unit = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add= True, editable=False)

    class Meta:
        ordering = ['-date', 'category']

    def __str__(self):
        return self.parameter
