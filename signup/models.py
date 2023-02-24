from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import URLValidator

class Client(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(User)
    password= models.CharField(max_length=8)
    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.client.save()



class Work(models.Model):
    link=models.TextField(validators=[URLValidator()])
    work_type=models.CharField(max_length=10)

class Artist(models.Model):
    name=models.CharField(max_length=30)
    work=models.ManyToManyField(Work)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


