from django.shortcuts import render
# from rest_framework import viewsets
# from invoice_app.models import Invoice
# from invoice_app.serializers import InvoiceSerializer

# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.prefetch_related('invoice_details')
#     serializer_class = InvoiceSerializer
from rest_framework import viewsets
from invoice_app.models import Invoice
from invoice_app.serializers import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.prefetch_related('details')
    serializer_class = InvoiceSerializer
