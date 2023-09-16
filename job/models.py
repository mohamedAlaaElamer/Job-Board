from typing import Any
from django.db import models

# Create your models here.
class Job(models.Model):
    types = [('Full Time','Full Time'),
             ('Part Time','Part Time'),
             ]
    


    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=20, choices=types)
    description = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title

