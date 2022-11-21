from django.contrib import admin
from django.urls import path

from project import views

urlpatterns = [
    path('', views.show_home),
    path('admin/', admin.site.urls),
]
