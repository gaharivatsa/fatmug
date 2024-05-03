from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder

class VendorAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_data = {'name': 'Test Vendor', 'contact_details': 'Test Contact', 'address': 'Test Address', 'vendor_code': 'TEST123'}

    def test_create_vendor(self):
        response = self.client.post(reverse('create_vendor'), self.vendor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 1)



class PurchaseOrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='Test Contact', address='Test Address', vendor_code='TEST123')
        self.po_data = {'po_number': 'PO123', 'vendor': self.vendor.id, 'order_date': '2024-05-05T00:00:00Z', 'items': ['item1'], 'quantity': 1, 'status': 'pending', 'issue_date': '2024-05-05T00:00:00Z'}

    def test_create_purchase_order(self):
        response = self.client.post(reverse('create_purchase_order'), self.po_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)







class VendorPerformanceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='Test Contact', address='Test Address', vendor_code='TEST123')

    def test_get_vendor_performance(self):
        url = reverse('get_vendor_performance', args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



