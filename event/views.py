from event import models

# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


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
    d = models.Date(date=date)
    d.save()
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
    event = models.EventConfig.objects.get(id=event_id)
    context = {"event": event}
    return render(requesut, "event/shousai.html", context)


def delete(request, event_id):
    event = models.EventConfig.objects.get(id=event_id)
    event.delete()
    return HttpResponseRedirect(reverse("event:list"))
