from django.contrib import admin
from pagi.models import Person, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['model', 'brand']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
    list_filter = ['name', 'car']
