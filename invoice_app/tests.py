
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        data = {
            'date': '2023-07-14',
            'invoice_no': 'INV-001',
            'customer_name': 'John Doe',
            'details': [
                {
                    'description': 'Item 1',
                    'quantity': 2,
                    'unit_price': '10.00',
                    'price': '20.00',
                },
                {
                    'description': 'Item 2',
                    'quantity': 1,
                    'unit_price': '15.00',
                    'price': '15.00',
                },
            ]
        }

        response = self.client.post('/api/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        invoice = Invoice.objects.get(pk=response.data['id'])
        serializer = InvoiceSerializer(invoice)
        self.assertEqual(response.data, serializer.data)
