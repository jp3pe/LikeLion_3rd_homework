'''
import some modules to make it run
'''
from django.db import models

# Create your models here.

class Blog(models.Model):
    '''
    Defined data structure at blog post
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    