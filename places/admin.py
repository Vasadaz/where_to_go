from django.contrib import admin
from django.utils.safestring import mark_safe

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
    fields = [
        'image',
        'preview',
        'position',
    ]
    list_display = (
        'place',
        'position',
        'image',
    )
    readonly_fields = ['preview']

    @admin.display()
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')
