from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=28)
    subject = models.CharField(max_length=28)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=255)
    submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

