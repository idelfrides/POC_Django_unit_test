from django.contrib import admin

from .models import Animal

# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'sound']

    class Meta:
        model = Animal


# @admin.register(Animal, AnimalAdmin)
admin.site.register(Animal, AnimalAdmin)