# Create your views here.

from todo1 import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    all_todo = models.Todo.objects.all()
    context = {"all_todo": all_todo}
    return render(request, "todo1/list.html", context)


def edit(request):
    return HttpResponse("Hello, world. You're at the todo1 edit.")


def register(request):
    title = request.POST.get("title")
    if title is None or title == "":
        return HttpResponseRedirect(reverse("todo1:list"))

    new_todo = models.Todo(title=title)
    new_todo.save()  # 登録する
    return HttpResponseRedirect(reverse("todo1:list"))  # 表示する
