from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def addbagitem(request):
    return render(request, "addbagitem.html")


def addmessage(request):
    return render(request, "addmessage.html")


def bag(request):
    return render(request, "myself.html")


def invitation(request):
    return render(request, "invitation.html")


def reci(request):
    return render(request, "reci.html")


def recipe(request):
    return render(request, "recipe.html")


def search(request):
    return render(request, "search.html")


def second(request):
    return render(request, "second.html")


def sign_in(request):
    return render(request, "sign_in.html")


def sign_up(request):
    return render(request, "sign_up.html")


def person(request):
    return render(request, "person.html")


def searchresult(request):
    return render(request, "sea_result.html")


def test(request):
    return render(request, "test2.html")
