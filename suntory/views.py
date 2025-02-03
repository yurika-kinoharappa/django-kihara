from django.shortcuts import render

from suntory import models

from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    all_s = models.santori.objects.all()
    dct = {"all_s": all_s}
    return render(request, "santori/index.html", dct)


def form(request):
    text = request.POST.get("text")
    sv = models.santori(text=text)
    sv.save()
    return HttpResponseRedirect(reverse("santori:index"))


def index2(request):
    all_s = models.santori.objects.all()
    dct = {"all_s": all_s}
    return render(request, "santori/form.html", dct)


def reaction(request, s_id):
    if "ganba" in request.POST:
        r = models.santori.objects.get(id=s_id)
        r.ganba += 1
    elif "daijobu" in request.POST:
        r = models.santori.objects.get(id=s_id)
        r.daijobu += 1
    elif "aruaru" in request.POST:
        r = models.santori.objects.get(id=s_id)
        r.aruaru += 1
    return HttpResponseRedirect(reverse("santori:index"))
