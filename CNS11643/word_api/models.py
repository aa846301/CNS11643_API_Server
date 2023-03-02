from django.db import models

# Create your models here.

class CharMap(models.Model):
    cns_code = models.CharField(max_length=7)
    unicode_code = models.CharField(max_length=5)
    big5_code = models.CharField(max_length=5)