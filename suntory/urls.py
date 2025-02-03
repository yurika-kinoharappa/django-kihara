from django.urls import path

from . import views

app_name = "santori"

urlpatterns = [
    path("", views.index, name="index"),
    path("index2", views.index2, name="index2"),
    path("form/", views.form, name="form"),
    path("reaction/<int:s_id>", views.reaction, name="reaction"),
]
