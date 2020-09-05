from django.db import models

# Create your models here.
class Config(models.Model):
    ip=models.CharField(max_length=255)
    site=models.CharField(max_length=255)
    identifiant=models.CharField(max_length=255)
    mot_de_passe=models.CharField(max_length=255)
    cle_local=models.CharField(max_length=255)
