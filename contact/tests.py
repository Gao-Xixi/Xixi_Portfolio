from django.core.checks import messages
from django.http import response
from django.test import TestCase
from .models import Contact
from django.urls import reverse
# Create your tests here.
class ContactTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="xiao", email='xiao@gmail.com', message="A Test!"
            )

    def test_string(self):
        contact = Contact(name="da")
        self.assertEqual(str(contact), contact.name)
    
    def test_get_absolute_url(self):
        self.assertEqual(self.contact.get_absolute_url(), '/projects/')

    def test_create_view(self):
        response = self.client.post(reverse('contact'),{
            'name': 'New name',
            'email': 'new@gmail.com',
            'message': 'New message'

        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Contact.objects.last().name,'New name')
        self.assertEqual(Contact.objects.last().email,'new@gmail.com')
        self.assertEqual(Contact.objects.last().message,'New message')