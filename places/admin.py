from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.utils.safestring import mark_safe

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    extra = 1
    model = Image
    fields = [
        'image',
        'preview',
        'position',
    ]
    readonly_fields = ['preview']

    @admin.display()
    def preview(self, obj):
        return preview(obj)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = (
        'title',
    )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = [
        'image',
        'preview',
        'position',
    ]
    list_display = (
        'position',
        'place',
        'preview',
    )
    readonly_fields = ['preview']

    @admin.display()
    def preview(self, obj):
        return preview(obj)


def preview(obj):
    return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')
