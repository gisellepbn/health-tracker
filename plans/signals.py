from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Profile
import os


@receiver(pre_delete, sender=Profile)
def delete_old_profile_picture(sender, instance, **kwargs):   
    try:
        path = Profile.objects.get(id=instance.id).picture.path
        
        if os.path.exists(path):           
            os.remove(path)        
    except:
        pass