from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image


@admin.display()
def preview(image: Image):
    return mark_safe(f'<img src="{image.file.url}" style="max-height: 200px;">')


class ImageInline(SortableTabularInline):
    extra = 1
    model = Image
    fields = [
        'file',
        preview,
        'position',
    ]
    readonly_fields = [preview]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = (
        'title',
    )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = [
        'place',
        'position',
        'file',
        preview,
    ]
    list_display = (
        'position',
        'place',
        preview,
    )
    readonly_fields = [preview]
