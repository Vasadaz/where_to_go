from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places.views import index, places

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('places/<int:place_id>/', places, name='places'),
    path('tinymce/', include('tinymce.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
