from event import models

# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


def form(request):
    # listのif文の到着点
    return render(request, "event/form.html")


def create(request):
    # 入力とってリストを表示
    title = request.POST.get("title")
    memo = request.POST.get("memo")
    if title is None or title == "":
        return HttpResponseRedirect(reverse("event:form"))
    e = models.EventConfig(name=title, memo=memo)
    e.save()
    return HttpResponseRedirect(reverse("event:list"))


def list(request):
    all_e = models.EventConfig.objects.all()
    context = {"all_e": all_e}
    return render(request, "event/list.html", context)


def sinnki(request):
    # 新規予定追加から作成ページへ
    return HttpResponseRedirect(reverse("event:form"))


def kiyaku(request):
    # 規約のページを表示
    return render(request, "event/kiyaku.html")


def kiyaku2(request):
    # 規約のページから作成ページへ
    return HttpResponseRedirect(reverse("event:form"))


def shousai(requesut):
    return render(requesut, "event/shousai.html")


def delete(request, event_id):
    event = models.EventConfig.objects.get(id=event_id)
    event.delete()
    return HttpResponseRedirect(reverse("event:list"))
