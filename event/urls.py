from django.urls import path

from . import views

app_name = "event"

urlpatterns = [
    path("", views.form, name="form"),
    path("create/", views.create, name="create"),
    path("list/", views.list, name="list"),
    path("sinnki/", views.sinnki, name="sinnki"),
    path("kiyaku/", views.kiyaku, name="kiyaku"),
    # path("", views.kiyaku, name="kiyaku2"),
    path("shousai/", views.shousai, name="shousai"),
    path("delete/<int:event_id>", views.delete, name="delete"),
]
