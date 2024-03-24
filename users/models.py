from django.db import models

# Create model user.
class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)