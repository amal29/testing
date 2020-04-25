from django.db import models

# Create your models here.
class tbl(models.Model):
  name=models.CharField(max_length=20)
  pas = models.CharField(max_length=20)