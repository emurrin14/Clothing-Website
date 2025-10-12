from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from clothes.emails import send_welcome_email

@receiver(post_save, sender=User)
def send_welcome_email_on_user_creation(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)
