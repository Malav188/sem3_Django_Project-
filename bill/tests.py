from django.test import TestCase
from .models import *

class MyModelTestCase(TestCase):
    def setUp(self):
        cosutomer_detailes.objects.create(name="Test Object")

    def test_model_name(self):
        obj = cosutomer_detailes.objects.get(name="Test Object")
        self.assertEqual(obj.name, 'Test Object')



