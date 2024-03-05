from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from django.core.mail import send_mail
from posts.models import News

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.save()

        subject = "NEW USER"
        message = f"Xush kelibsiz!, Добро пожаловать!, Welcome!-- {instance.username}"
        from_email = 'humoyunakbaraliyev2159555@gmail.com'
        to_email = instance.email

        send_mail(subject, message, from_email, [to_email])


@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    instance.profile.delete()


@receiver(post_save, sender=News)
def new_post(sender, instance, created, **kwargs):
    if created:
        users = User.objects.exclude(pk=instance.user.pk)
        subject = f"NEW POST: {instance.title}"
        post_detail = reverse('DetailNews', args=[instance.id])
        message = f"\n\n{instance.content[:20]}...\n\nContinue reading here: <a href='http://localhost:8000{post_detail}' style='text-decoration: none'>Read More</a>"
        from_mail = 'humoyunakbaraliyev2159555@gmail.com'

        for user in users:
            to = user.email
            send_mail(subject, message, from_mail, [to], html_message=message)


