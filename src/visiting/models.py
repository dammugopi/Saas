from django.db import models

# Create your models here.
class Page_visits(models.Model):
  path=models.TextField(blank=True,null=True)
  timestampp= models.DateTimeField( auto_now_add=True)