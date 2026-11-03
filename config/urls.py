from django.contrib import admin
from django.urls import path

from shortener.views import short_link

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("<path:path>/", short_link, name="short_link"),
]
