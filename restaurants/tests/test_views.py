from django.test import TestCase, Client
from django.urls import reverse
from restaurants.models import Place, Menu
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.place_url = reverse('home')

        self.place_list_url = reverse('place_list', args=['testing', 1])
        self.place1 = Place.objects.create(
            name='testing',
            address='Baker Street 13',
            number_phone='982223123',
            hours='PN-PT: 9-23',
            news='Blank Data',
            description='information about this place'
        )
        

    def test_homepage_GET(self):
        client = Client()
        response = self.client.get(self.place_url)

        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_place_list_GET(self):
        client = Client()
        response = self.client.get(self.place_list_url)

        self.assertAlmostEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'place_list.html')