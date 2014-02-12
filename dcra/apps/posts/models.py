from django.db import models
from .tasks import mul


class Post(models.Model):
    title = models.TextField()

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        result = mul.delay(1, 4)

    def __str__(self):
        return self.title