from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class ApiData(models.Model):
    
    Id = models.UUIDField(primary_key=True, editable=False)
    access_token = models.fields.TextField()
    refresh_token = models.TextField()
