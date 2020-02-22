from django.db import models

# Create your models here.

class Word(models.Model):
    title = models.CharField(max_length = 50)
    pub_date = models.DateTimeField(auto_now=True)
    writer = models.CharField(max_length = 50)
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]