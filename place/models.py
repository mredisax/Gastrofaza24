from django.db import models
from django.urls import reverse

class Place(models.Model):
    name = models.CharField('Nazwa lokalu', max_length=200)
    img = models.ImageField('Zdjęcie Lokalu', upload_to='Place/static/locals/img', blank=True, max_length=500)
    address = models.CharField('Adres', max_length=1000)
    number_phone = models.CharField('Numer telefonu', max_length=26)
    hours = models.TextField(verbose_name='Godziny otwarcia', max_length=2000)
    news = models.TextField('Aktualności', default='', blank=True, max_length=2000)
    maps = models.CharField('Mapa', default='',blank=True, max_length=1000)
    status = models.BooleanField('Opublikuj', default=False)
    
    class Meta:
        verbose_name = 'Lokal'
        verbose_name_plural = 'Lokale'
    def __str__(self):
        return self.name

class Menu(models.Model):
    place = models.ForeignKey(Place, related_name='place', on_delete=models.CASCADE)
    pizza = 'Pizza'
    kebab = 'Kebab'
    burgery = 'Burgery'
    kanapki = 'Kanapki'
    salatki = 'Sałatki'
    napoje = 'Napoje'
    inne = 'Inne'
    cat_dish = (
        (pizza, 'Pizza'),
        (kebab, 'Kebab'),
        (burgery, 'Burgery'),
        (kanapki, 'Kanapki'),
        (salatki, 'Sałatki'),
        (napoje, 'Napoje'),
        (inne, 'Inne'),
    )
    dish = models.CharField('Nazwa Potrawy', blank=True, max_length=200)
    dish_components = models.CharField("Składniki", blank=True, default="", max_length=1200)
    dish_category = models.CharField("Kategoria", default="Kategoria", choices=cat_dish, max_length=200)
    pizza_price = models.CharField("Rozmiar i cena Pizzy", help_text="np.Mała-10zł", default="", blank=True, max_length=300) 
    price = models.DecimalField("Cena",default="00", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'