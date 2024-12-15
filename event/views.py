from event import models

# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


def form(request):
    # listのif文の到着点
    return render(request, "event/form.html")


def list(request):
    # 入力とってリストを表示
    title = request.POST.get("title")
    if title is None or title == "":
        return HttpResponseRedirect(reverse("event:form"))
    e = models.EventConfig(name=title)
    # e.save()
    all_e = models.EventConfig.objects.all()
    context = {"all_e": all_e}
    memo = request.POST.get("memo")
    memo = models.EventConfig(memo=memo)
    obj = models.EventConfig(name=e, memo=memo)
    obj.save()
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
