from django.db import models

# Create your models here.


class Post (models.Model):
    text = models.TextField()

    def __string__(self):
        return self.text[:50]
