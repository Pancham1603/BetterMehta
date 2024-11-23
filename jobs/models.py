from django.db import models
import uuid

# Create your models here.
class PrintJob(models.Model):
    name = models.CharField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)
    ready_by_time = models.DateTimeField()
    eta = models.IntegerField()
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_priority = models.BooleanField(default=False)
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False)
    preferences = models.JSONField(default=dict)
    document_id = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=200)


    def __str__(self):
        return self.name