from django.db import models
import uuid


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class ApiData(models.Model):

    Id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    access_token = models.fields.TextField()
    refresh_token = models.TextField()
