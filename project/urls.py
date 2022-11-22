from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from project import views

urlpatterns = [
    path('', views.show_home),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
