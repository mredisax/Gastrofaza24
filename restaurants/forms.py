from django import forms
from .models import Place, Menu
# from captcha.fields import ReCaptchaField


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ('name', 'img', 'address', 'number_phone', 'hours', 'news', 'description',)


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('dish', 'dish_components','dish_category', 'pizza_price', 'price',)

class AboutForm(forms.Form):
    email = forms.EmailField(max_length=300, required=True)
    temat = forms.CharField(required=True)
    wiadomosc = forms.CharField(widget=forms.Textarea, required=True)
    # captcha = ReCaptchaField()
