from django.db import models
import uuid

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    student_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name