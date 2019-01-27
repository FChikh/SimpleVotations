from django.shortcuts import render


def login_page(request):
    return render(request, "login.html", {})


def singup_page(request):
    return render(request, "singin.html", {})
