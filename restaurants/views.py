from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from .models import Place, Menu
from .forms import PlaceForm, MenuForm, AboutForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.forms import formset_factory, inlineformset_factory


def homepage_view(request):
    places = Place.objects.filter(status = True)
    context = {
        'places': places
    }    
    return render(request, 'index.html', context)

def place_list_view(request, slug, id):
    query_pk_and_slug = True
    place = Place.objects.get(id=id, slug=slug)
    menu = Menu.objects.filter(place_id=id).order_by('id')
    context = {
        'place': place,
        'menu': menu
    }
    return render(request, 'place_list.html', context)

def place_create_view(request, id=id):
    form = PlaceForm()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            obj = form.save()
            useremail = request.user.email
            text_msg = render_to_string('email.txt', {'place_id': obj.id})
            html_msg = render_to_string('email.html', { 'place_id': obj.id})
            send_mail(
                'Dodaj Menu',
                text_msg,
                'your_email@example.com',
                [useremail],
                html_message=html_msg,
                )
            return render(request, 'success.html')
        else:
            return render(request, 'failed.html')

    context = {
        'form': form
    }
    return render(request, 'place_create.html', context)

def menu_create_view(request, id=id):
    obj = get_object_or_404(Place, id=id)
    MenuFormset = inlineformset_factory(Place, Menu, can_delete=True, fields=('dish', 'dish_components', 'dish_category', 'price',), extra=1, max_num=3000)
    form = PlaceForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        formset = MenuFormset(request.POST, instance=obj)
        if formset.is_valid():
            formset.save(commit=False)
            formset.save()
        else:
            pass
        if form.is_valid():
            form.save()
    formset = MenuFormset(instance=obj)
    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'menu_add.html', context)
    
def place_about_view(request):
    form = AboutForm(request.POST)
    if form.is_valid():
        temat = form.cleaned_data['temat']
        email = form.cleaned_data['email']
        wiadomosc = form.cleaned_data['wiadomosc']
        try:
            send_mail(temat, wiadomosc, email, ['your_email@example.com'], fail_silently=False)
        except:
            return HttpResponse('Błąd')
        return render(request, 'successmail.html')
    else:
        form = AboutForm()
    return render(request, "about.html", {'form': form})

# def handler404(request):
    # return render(request, '404.html', status=404)

# def handler500(request):
    # return render(request, '500.html', status=500)
