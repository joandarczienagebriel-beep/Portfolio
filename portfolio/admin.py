from django.contrib import admin
from .models import Info, Portfolio

class InfoAdmin(admin.ModelAdmin):
    list_display=[
        "name",
        "email",
        "services",
        "message",
    ]

class PortAdmin(admin.ModelAdmin):
    list_display=[
        "title",
        "body",
    ]

admin.site.register(Info, InfoAdmin)
admin.site.register(Portfolio, PortAdmin)

# Register your models here.
