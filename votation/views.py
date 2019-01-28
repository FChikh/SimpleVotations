from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def profile(request):
    return render(request, "profile.html")
