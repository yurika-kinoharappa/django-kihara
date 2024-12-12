from django.urls import path

from . import views

app_name = "todo1"

urlpatterns = [
    path("list/", views.index, name="list"),
    path("edit/", views.edit, name="edit"),
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
]
