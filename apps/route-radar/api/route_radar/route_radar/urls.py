from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from .api import api

api = NinjaAPI()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
