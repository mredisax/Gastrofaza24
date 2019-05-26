from django.shortcuts import render, get_object_or_404, redirect
from .models import Place, Menu
from .forms import PlaceForm, MenuForm

def homepage_view(request):
    places = Place.objects.filter(status = True)
    context = {
        'places': places
    }
    return render(request, "index.html", context)

def place_list_view(request, id):
    place = Place.objects.get(id=id)
    menu = Menu.objects.filter(place_id=id).order_by('dish_category')
    context = {
       'place' : place,
       'menu' : menu
    }
    return render(request, "place_list.html", context)

def place_create_view(request):
    form = PlaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PlaceForm()
        return redirect("place_create.html")
    context = {
        'form': form
    }
    return render(request, "forms.html", context)