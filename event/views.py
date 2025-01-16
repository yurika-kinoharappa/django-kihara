from event import models

# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
import datetime


def form(request):
    # フォームを表示する
    return render(request, "event/form.html")


def create(request):
    # 入力とって登録
    title = request.POST.get("title")
    memo = request.POST.get("memo")
    date = request.POST.get("date")
    created_date = request.POST.get("created_date")
    if title is None or title == "":
        return HttpResponseRedirect(reverse("event:form"))
    e = models.EventConfig(name=title, memo=memo)
    e.save()
    cd = models.CreatedDate(created_at=created_date)
    cd.save()
    d = date.split()
    dat = models.Date(day=d[0], time1=str(d[1]), time2=str(d[2]))
    dat.save()
    return HttpResponseRedirect(reverse("event:list"))


def list(request):
    # リストを表示
    all_e = models.EventConfig.objects.all()
    context = {"all_e": all_e}
    return render(request, "event/list.html", context)


def kiyaku(request):
    # 規約のページを表示
    return render(request, "event/kiyaku.html")


def shousai(requesut, event_id):
    # 詳細
    event = models.EventConfig.objects.get(id=event_id)
    date = models.Date.objects.get(id=event_id)
    d1 = date.time1.strftime("%H時%M分")
    d2 = date.time2.strftime("%H時%M分")
    Y, M, D = date.day.split("-")
    Y = int(Y)
    M = int(M)
    D = int(D)
    ddd = datetime.date(Y, M, D)
    w = ddd.strftime("%a")
    createddate = models.CreatedDate.objects.get(id=event_id)
    c = createddate.created_at.strftime("%Y-%m-%d")
    a, b, c = c.split("-")
    a = int(a)
    b = int(b)
    c = int(c)
    dd = datetime.date(a, b, c)
    week = dd.strftime("%a")
    context = {
        "event": event,
        "a": a,
        "b": b,
        "c": c,
        "Y": Y,
        "M": M,
        "D": D,
        "createddate": c,
        "date": date,
        "time1": d1,
        "time2": d2,
        "week": week,
        "w": w,
    }
    return render(requesut, "event/shousai.html", context)


def delete(request, event_id):
    event = models.EventConfig.objects.get(id=event_id)
    event.delete()
    return HttpResponseRedirect(reverse("event:list"))


def change(requet, event_id):
    return HttpResponseRedirect(reverse("event:list"))
