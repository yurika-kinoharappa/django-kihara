from django.http import HttpResponse


def list(request):
    return HttpResponse("Hello, world. You're at the todo2 list.")


def edit(repuest):
    return HttpResponse("Hello, world. You're at the todo2 edit.")
