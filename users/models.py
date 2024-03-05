from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.URLField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fdefault&psig=AOvVaw2Cux9WSXZRad0Bo9SPG5Pq&ust=1709720822210000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCKD2vcT03IQDFQAAAAAdAAAAABAE')

    def __str__(self):
        return self.user.username

