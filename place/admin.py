from django.contrib import admin
from .models import Place, Menu
from django.forms import Textarea
from django.db.models.fields import TextField

class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0 
    max_num = 2000

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    exclude = ('autor',)
    inlines = [MenuInline]
    list_display =('name', 'status')
    search_fields = ['']
    list_per_page = 10
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 35})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()

