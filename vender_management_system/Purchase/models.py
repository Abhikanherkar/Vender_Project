from django.db import models
from Vender.models import Vender

# Create your models here.


class Purchase(models.Model):
    StatusChoices = [
    ("Pending", "Pending"),
    ("Completed", "Completed"),
    ("Canceled", "Canceled"),
    ("Aknowledged", "'Aknowledged")]

    po_number = models.CharField(max_length = 30, unique = True) 
    vendor = models.ForeignKey(Vender, on_delete = models.CASCADE, related_name = 'vender_purchase')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length = 50, choices=StatusChoices, default = 'Pending')
    quality_rating = models.FloatField(default=0)
    issue_date = models.DateTimeField(auto_now_add = True)
    acknowledgment_date = models.DateTimeField(null = True)
    completed_date = models.DateTimeField(null = True)

class HistoryPerfoemence(models.Model):
    vendor = models.ForeignKey(Vender, on_delete = models.CASCADE, related_name = 'vender_performence')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()



class PurchaseStatusLog(models.Model):
    prchase_id = models.ForeignKey(Purchase, related_name = "purchase_log", on_delete = models.CASCADE)
    status = models.CharField(max_length = 50)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now = True)