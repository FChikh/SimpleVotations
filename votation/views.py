from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from random import randint
from votation import models
from votation import votingEngine
from votation.forms import ProfileEditForm


def main(request):  # main page
    data = dict()
    data = votingEngine.friendly_extract_for_everyone()
    return render(request, "main.html", data)


def complain(request):  # complain page
    data = {}
    return render(request, "complaints.html", data)


def metro(request):  # easter egg
    return render(request, 'newmetro.html')


def game(request):  # easter egg
    return render(request, ["snake.html", "game2.html"][randint(0, 1)], {})


@login_required
def new_vote(request):  # getting data from form
    data = dict()
    # print(request)
    if request.method == "POST":
        votingEngine.addvoting(request)
        return redirect('/')

    return render(request, "new_vote.html", data)


@login_required
def profile(request):  # main func to form all the data for a profile cout

    data = dict()

    data = (votingEngine.friendly_extract_for_profile(request.user.id))

    data['name'] = request.user.username
    data['surname'] = request.user.email
    # print(data)

    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            try:
                user_old = User.objects.get(username=data['name'])
                new_username = form.data.get('username')
                new_email = form.data.get('email')
                # print(new_username, new_email)
                u = User.objects.get(username=data['name'])
                u.email = new_email
                u.username = new_username
                u.save()
                if form.data.get('password') is not '':
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


def voting(request):
    if request.method in ["GET", "POST"]:
        id = request.GET["id"]
        dat = models.VotingsBase.objects.filter(id=id).values_list()

        dat = dat[0]
        res = {}
        vars = []
        res['id'] = dat[0]
        res['authorid'] = dat[1]
        res['maintitle'] = dat[2]
        res['cnt'] = 0

        for i in range(4, 4 + dat[3] * 2, 2):
            vars.append([dat[i], dat[i + 1]])
            res['cnt'] += int(dat[i + 1])
        res['variants'] = vars
        for i in vars:
            if res['cnt'] != 0:
                i.append(round(int(i[1]) / res['cnt'] * 100))
            else:
                i.append(15)
        return render(request, "voting.html", res)
    return render(request, "voting.html")


def logout_func(request):
    logout(request)
    return redirect('/')