from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render
from random import randint

from votation import votingEngine
from votation.forms import ProfileEditForm


def main(request):
    data = dict()
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

def metro(request):
    return render(request,'newmetro.html')
def game(request):
    return render(request, ["snake.html", "game2.html"][randint(0, 1)], {})


def new_vote(request):
    data = dict()
    print(request)
    if request.method == "POST":
        votingEngine.addvoting(request)

    return render(request, "new_vote.html", data)


@login_required
def profile(request):
    data = dict()

    data = (votingEngine.friendly_extract_for_profile(request.user.id))

    data['name'] = request.user.username
    data['surname'] = request.user.email
    print(data)

    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            try:
                user_old = User.objects.get(username=data['name'])
                new_username = form.data.get('username')
                new_email = form.data.get('email')
                if new_username is None:
                    new_username = user_old.username
                if new_email is None:
                    new_email = user_old.email
                print(new_username, new_email)
                u = User.objects.get(username=data['name'])
                u.email = new_email
                u.username = new_username
                if form.data.get('password') is not None:
                    u.password = ''
                    u.set_password(form.data.get('password'))
                    update_session_auth_hash(request, u)
                u.save()
                logout(request)
                login(request, u)
                data['name'] = new_username
                data['surname'] = new_email

            except IntegrityError:
                messages.error(request, 'Пользователь с таким логином уже существует')
                return render(request, 'profile.html', data)
        else:
            return render(request, 'profile.html', data)
    return render(request, "profile.html", data)
