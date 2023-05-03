from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import Profile
import os


@receiver(pre_save, sender=Profile)
def delete_old_profile_picture_on_update(sender, instance, **kwargs):
    if instance.id:
            try:
                old_picture = Profile.objects.get(id=instance.id).picture                
            except Profile.DoesNotExist:
                return
            else:
                new_picture = instance.picture
                if old_picture and old_picture.url != new_picture.url:
                    old_picture.delete(save=False)


@receiver(pre_delete, sender=Profile)
def delete_old_profile_picture(sender, instance, **kwargs):   
    try:
        path = Profile.objects.get(id=instance.id).picture.path
        
        if os.path.exists(path):           
            os.remove(path)        
    except:
        pass