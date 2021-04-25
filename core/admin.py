from django.contrib import admin
from core.models import GhostName

# Register your models here.

class GhostNameAdmin(admin.ModelAdmin):
    """
    BASI DJANGO ADMIN FOR MANUAL GOSHT CREATION OR EDITTION
    """

    fieldsets = (
        ('Ghost detials', {
            "fields": ("name", "description")}),
        ('Owner information', {
            "fields": ("user", 'first_name', 'last_name')}),
    )

    list_display = [ 'name', 'first_name', 'last_name']

admin.site.register(GhostName, GhostNameAdmin)