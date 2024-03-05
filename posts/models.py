from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.URLField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    viewers = models.IntegerField(default=0)

    class Meta:
        db_table = 'News'

    def __str__(self):
        if len(self.title) > 40:
            return f"{self.title[:40]}..."
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.comment) > 40:
            return f"{self.comment[:40]}..."
        return self.comment
