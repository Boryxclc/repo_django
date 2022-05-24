from django.db import models

# Create your models here.
class familia(models.Model):
    profetion=(
       ('ingeniero','ingeniero'),
       ('medico','medico'),
       ('profesor','profesor'),
    )
    date_birth = models.DateField()
    firts_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    education = models.CharField(max_length=30, choices=profetion)
   