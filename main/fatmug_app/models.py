from django.db import models
from django.db.models import Count, Avg
from datetime import timedelta


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)

    def on_time_delivery_rate(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()
        if total_completed_pos == 0:
            return 0.0
        on_time_pos = completed_pos.filter(delivery_date__lte=models.F('expected_delivery_date'))
        on_time_pos_count = on_time_pos.count()
        return (on_time_pos_count / total_completed_pos) * 100

    def quality_rating_avg(self):
        completed_pos = self.purchaseorder_set.filter(status='completed').exclude(quality_rating=None)
        if completed_pos.count() == 0:
            return 0.0
        return completed_pos.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']

    def average_response_time(self):
        completed_pos = self.purchaseorder_set.filter(status='completed').exclude(acknowledgment_date=None)
        if completed_pos.count() == 0:
            return 0.0
        response_times = completed_pos.annotate(response_time=models.F('acknowledgment_date') - models.F('issue_date'))
        avg_response_time = response_times.aggregate(avg_response_time=Avg('response_time'))['avg_response_time']
        return avg_response_time.total_seconds() / 3600  

    def fulfillment_rate(self):
        total_pos = self.purchaseorder_set.count()
        if total_pos == 0:
            return 0.0
        fulfilled_pos = self.purchaseorder_set.filter(status='completed')
        return (fulfilled_pos.count() / total_pos) * 100

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
