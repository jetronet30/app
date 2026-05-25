from django.contrib import admin
from django.http import request
from django.urls import include, path
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
]
