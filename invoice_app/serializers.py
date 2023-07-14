from rest_framework import serializers
from invoice_app.models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ('id', 'description', 'quantity', 'unit_price', 'price')

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'invoice_no', 'customer_name', 'invoice_details')

    def get_invoice_details(self, instance):
        invoice_details = InvoiceDetail.objects.filter(invoice=instance)
        serializer = InvoiceDetailSerializer(invoice_details, many=True)
        return serializer.data

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice_details', [])
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in invoice_details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice
