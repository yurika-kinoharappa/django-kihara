from event import models
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# from django.shortcuts import render


def index(request):
    e = models.EventConfig(name="patry")
    # e = models.EventConfig(name="party")
    e.save()
    all_e = models.EventConfig.objects.all()
    return HttpResponse(all_e)


def list(request):
    return HttpResponse("Hello, world. You're at the event list.")


def form(request):
    return HttpResponseRedirect(reverse("event:list"))
