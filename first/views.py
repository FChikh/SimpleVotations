from django.shortcuts import render


def index_page(request):
    return render(request, "index.html", {})


def login_page(request):
    return render(request, "login.html", {})


def singup_page(request):
    return render(request, "singin.html", {})
