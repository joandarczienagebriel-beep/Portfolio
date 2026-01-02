from django.contrib import admin
from .models import Point, GradeTen

class PointAdmin(admin.ModelAdmin):
    list_display=[
        "author",
        "name",
        "math",
        "biology",
        "chemistry",
        "physics",
    ]
    search_fields=['name']

class Grade_tenAdmin(admin.ModelAdmin):
    list_display=[
        "author",
        "name",
        "math",
        "biology",
        "chemistry",
        "physics",
    ]
admin.site.register(Point, PointAdmin)
admin.site.register(GradeTen, Grade_tenAdmin)

# Register your models here.
