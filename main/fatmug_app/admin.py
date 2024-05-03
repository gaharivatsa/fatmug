from django.contrib import admin
from .models import Vendor, PurchaseOrder

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    pass

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    pass