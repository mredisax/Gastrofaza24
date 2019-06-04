from django import forms
from .models import Place, Menu


class PlaceForm(forms.ModelForm):
    
    class Meta:
        model = Place
        fields = ('name', 'img','address','number_phone','hours','news',)

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('dish', 'dish_components','dish_category', 'pizza_price', 'price',)
