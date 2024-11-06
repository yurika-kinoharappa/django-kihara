from django.http import HttpResponse
from .models import EventConfig
from django.shortcuts import render


def index(request):
    latest_question_list = EventConfig.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "event/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def create(request):
    # 画面で入力した名前をとってくる
    # name = cxxxxx
    e = EventConfig(name="party")
    e.save()
    return HttpResponse("You're voting on question")
