from django.db import models
import uuid

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    is_online = models.BooleanField(default=False)
    preferences = models.JSONField(default=dict)
    currency = models.CharField(max_length=200)

    def __str__(self):
        return self.name