from event import models

# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


def form(request):
    return render(request, "event/form.html")


def list(request):
    title = request.POST.get("title")
    if title is None or title == "":
        return HttpResponseRedirect(reverse("event:form"))
    e = models.EventConfig(name=title)
    e.save()
    all_e = models.EventConfig.objects.all()
    context = {"all_e": all_e}
    return render(request, "event/list.html", context)


def index(request):
    return HttpResponseRedirect(reverse("event:list"))
