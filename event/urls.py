from django.urls import path

from . import views

app_name = "event"

urlpatterns = [
    path("", views.form, name="form"),
    path("create/", views.create, name="create"),
    path("list/", views.list, name="list"),
    path("kiyaku/", views.kiyaku, name="kiyaku"),
    path("shousai/<int:event_id>", views.shousai, name="shousai"),
    path("delete/<int:event_id>", views.delete, name="delete"),
    path("change/<int:event_id>", views.change, name="change"),
]
