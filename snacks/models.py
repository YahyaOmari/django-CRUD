from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Snack(models.Model):
    title = TextField()
    purchaser = TextField()
    description = TextField()
