from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from votation import votingEngine
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


    data = (votingEngine.friendly_extract_for_profile(1))
    print(data)
    data['name'] = request.user.username
    data['surname'] = request.user.email
    print(data)

    return render(request, "profile.html", data)
