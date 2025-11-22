from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # Link UserProfile to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra fields
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Optional: user preferences or other info can be added here later
    # example: wishlist, newsletter_subscription, etc.

    def __str__(self):
        return self.user.username


# SIGNALS — Automatically create or save UserProfile when User is created/updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
