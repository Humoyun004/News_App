from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOz18-'
                                            'q0kyakVcxdTuLlyyHVN5npGJi92ou04GZgFVLNWhTim5JlQBwA1hPJMzM90_Uas&usqp=CAU')

    def __str__(self):
        return self.user.username

