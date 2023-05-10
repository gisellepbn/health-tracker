from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Profile(AbstractUser):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    picture = models.ImageField(blank=True,null=True, upload_to='profile/', default='profile/default.png')
    created = models.DateTimeField(auto_now_add= True, editable=False)

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

    UNITS = [
        ('Calories', 'Calories'),
        ('Cups', 'Cups'),
        ('Grams', 'Grams'),
        ('Hours', 'Hours'),
        ('Kilograms', 'Kilograms'),
        ('Liters', 'Liters'),
        ('Minutes', 'Minutes'),
        ('Ounces', 'Ounces'),
        ('Portions', 'Portions'),
        ('Pounds', 'Pounds'),
        ('Repetitions', 'Repetitions'),
        ('Servings', 'Servings'),
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORIES)
    parameter = models.CharField(max_length=200)
    goal = models.FloatField()
    progress = models.FloatField(blank=True, null=True, default=0)
    unit = models.CharField(max_length=100, choices=UNITS)
    created = models.DateTimeField(auto_now_add= True, editable=False)

    class Meta:
        ordering = ['-date', 'category']

    def __str__(self):
        return self.parameter


    def serialize(self):
        return {
            "id": self.id,
            "profile": self.profile.username,
            "date": self.date,
            "category": self.category,
            "parameter": self.parameter,
            "goal": self.goal,
            "progress": self.progress,
            "unit": self.unit,
            "created": self.created           
        }