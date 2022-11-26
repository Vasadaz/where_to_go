from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = (
        'title',
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
