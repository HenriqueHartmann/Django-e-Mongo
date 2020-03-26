from django.contrib import admin
from django.urls import include, path

from DjangoMongo.core.views import router

urlpatterns = [path("", include(router.urls)), path("admin/", admin.site.urls)]
