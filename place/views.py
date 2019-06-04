from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Place, Menu
from .forms import PlaceForm, MenuForm
from django.forms import formset_factory, inlineformset_factory
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User

def homepage_view(request):
    places = Place.objects.filter(status = True)
    context = {
        'places': places
    }
    return render(request, "index.html", context)

def place_list_view(request,slug, id):
    query_pk_and_slug = True
    place = Place.objects.get(id=id, slug=slug)
    menu = Menu.objects.filter(place_id=id)
    context = {
       'place' : place,
       'menu' : menu
    }
    return render(request, "place_list.html", context)

def place_create_view(request, id=id):
    form = PlaceForm()
    success = False
    if request.POST:
        form = PlaceForm(request.POST)
        if form.is_valid():
            obj = form.save()
            useremail = request.user.email
            text_msg = render_to_string('email.txt', {'place_id': obj.id})
            html_msg = render_to_string('email.html', { 'place_id': obj.id})
            send_mail(
                'Dodaj Menu',
                text_msg, 
                'kontakt@gastrofaza24.pl', 
                [useremail],
                html_message=html_msg,
                )
            return render(request, "success.html")
    context = {
        'form': form
    }
    return render(request, "forms.html", context) 

def menu_create_view(request, id=id):
    obj = get_object_or_404(Place, id=id)
    MenuFormset = inlineformset_factory(Place, Menu, can_delete=True, fields=('dish','dish_components', 'price',),extra=1)
    form = PlaceForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        formset = MenuFormset(request.POST, instance=obj)
        if formset.is_valid():
            formset.save(commit=False)
            formset.save()

    if form.is_valid():
        form.save()
    formset = MenuFormset(instance=obj)
    context = {
        'form': form,
        'formset': formset
    }
    return render(request, "menu_add.html", context)

