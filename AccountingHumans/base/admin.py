from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Man)
class ManAdmin(admin.ModelAdmin):
    pass


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    pass
