from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def profile(request):
    data = {}
    data['name'] = "Игорь"
    data['surname'] = "Нуруллаев"
    data['pic'] = "static/votation/anon.png"
    return render(request, "profile.html", data)
