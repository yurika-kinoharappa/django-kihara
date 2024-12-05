from django.http import HttpResponse
from .models import EventConfig
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = EventConfig.objects.order_by("-id")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "event/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(EventConfig, pk=question_id)
    return render(request, "event/results.html", {"question": question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def create(request):
    # 画面で入力した名前をとってくる
    # name = cxxxxxx
    e = EventConfig(name="party")
    e.save()
    return HttpResponse("You're voting on question")
