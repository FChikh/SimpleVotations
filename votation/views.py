from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def main(request):
    data = {}
    data["votes"] = [
        [
            {
                "title": "Собачки",
                "percentage": 10
            },
            {
                "title": "Котики",
                "percentage": 20
            },
            {
                "title": "Единая Россия",
                "percentage": 70
            }
        ]
    ]
    # Хардкод
    data["votes"] *= 10
    return render(request, "main.html", data)


def complain(request):
    data = {}
    return render(request, "complaints.html", data)

@login_required
def profile(request):
    data = {}
    username = None
    username = request.user.username
    data['name'] = username
    data['surname'] = request.user.email
    data["votes_history"] = [
        [
            {
                "title": "Собачки",
                "percentage": 10
            },
            {
                "title": "Котики",
                "percentage": 20
            },
            {
                "title": "Единая Россия",
                "percentage": 70
            }
        ]
    ]
    # Хардкод
    data["votes_history"] *= 10
    return render(request, "profile.html", data)
