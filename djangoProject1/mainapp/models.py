from django.db import models

# Create your models here.
from django.db import models
class Design(models.Model):
    bg_color = models.CharField(max_length=7, null=False, blank=False)
    main_color = models.CharField(max_length=7, null=False, blank=False)
    length = models.PositiveIntegerField(null=False, blank=False)
    width = models.PositiveIntegerField(null=False, blank=False)
    style = models.CharField(max_length=10, null=False, blank=False)
    image = models.ImageField(upload_to='images/', null=False, blank=False)


class Contacts(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)