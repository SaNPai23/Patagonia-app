from django.db import models

# Create your models here.
from django.db import models


class Physician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)


class Patient(models.Model):
    physician_id = models.ForeignKey(Physician, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=150, unique=True)
