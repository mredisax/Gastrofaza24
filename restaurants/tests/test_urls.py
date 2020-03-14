from django.test import SimpleTestCase
from django.urls import reverse, resolve
from restaurants.views import homepage_view, \
                        place_about_view, \
                        place_create_view, \
                        place_list_view, \
                        menu_create_view
                            


class TestUrls(SimpleTestCase):

    def test_hompage_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, homepage_view)

    def test_place_list_url(self):
        url = reverse('place_list', args=['somelink', 5])
        self.assertEquals(resolve(url).func, place_list_view)

    def test_about_url(self):
        url = reverse('place_about')
        self.assertEquals(resolve(url).func, place_about_view)
    
    def test_place_create_url(self):
        url = reverse('place_create')
        self.assertEquals(resolve(url).func, place_create_view)

    def test_menu_create_url(self):
        url = reverse('menu_create', args=[5])
        self.assertEquals(resolve(url).func, menu_create_view)
    
    
