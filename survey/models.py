from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
class ResponsesBeta(models.Model):
	data = JSONField()