from django.db import models
from django import forms

# Create your models here.
PROGRAME_OPTION = (
    ('ft', 'Fulltime Football Program'),
    ('sc', 'Short-Course Football Programe'),
    ('tr', 'Showcase Matches(Try-outs)'),
)

class Register(models.Model):
    firstname = models.CharField(max_length=28)
    lastname = models.CharField(max_length=28)
    programe_option = models.CharField(max_length=28, choices=PROGRAME_OPTION)
    submitted = models.DateField(auto_now_add=True)

    email = models.EmailField(max_length=255, unique=True, error_messages={'unique':'This E-mail has already been registered'})
    
    def __str__(self):
        return str(self.id)
