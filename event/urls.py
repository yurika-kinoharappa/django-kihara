from django.urls import path

from . import views

app_name = "event"

urlpatterns = [
    path("", views.form, name="form"),
    path("list/", views.list, name="list"),
    path("index/", views.index, name="index"),
]
