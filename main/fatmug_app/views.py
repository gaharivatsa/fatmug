from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST 



@api_view(['POST'])
def create_vendor(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_vendors(request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = VendorSerializer(vendor)
    return Response(serializer.data)

@api_view(['PUT'])
def update_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = VendorSerializer(vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_vendor(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    vendor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def create_purchase_order(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_purchase_orders(request):
    purchase_orders = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PurchaseOrderSerializer(purchase_order)
    return Response(serializer.data)

@api_view(['PUT'])
def update_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    purchase_order.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@require_POST
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return JsonResponse({'error': 'Purchase Order does not exist'}, status=404)
    
    acknowledgment_date = request.POST.get('acknowledgment_date')
    if acknowledgment_date:
        purchase_order.acknowledgment_date = acknowledgment_date
        purchase_order.save()
        return JsonResponse({'success': 'Purchase Order acknowledged successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Acknowledgment date missing'}, status=400)
    
def get_vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    performance_metrics = {
        'on_time_delivery_rate': vendor.on_time_delivery_rate(),
        'quality_rating_avg': vendor.quality_rating_avg(),
        'average_response_time': vendor.average_response_time(),
        'fulfillment_rate': vendor.fulfillment_rate()
    }
    return JsonResponse(performance_metrics)