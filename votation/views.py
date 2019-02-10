from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from random import randint
from votation import models
from votation import votingEngine
from votation.forms import ProfileEditForm, Report
from votation.forms import ProfileEditForm
from datetime import datetime

def main(request):  # main page
    data = dict()
    data = votingEngine.friendly_extract_for_everyone()
    return render(request, "main.html", data)


@login_required
def complain(request):  # complain page
    if request.method == "POST":
        form = Report(request.POST)
        print(form)
        if form.is_valid():
            u = models.ReportsHistory.objects.create(text=form.data.get('report'),
                                                     author=request.user,
                                                     status="Не решена",
                                                     answer="")
            u.save()
            messages.success(request, "Ваша жалоба успешно отправлена")
    if request.method in ["POST", "GET"]:
        context = dict()
        context["history"] = models.ReportsHistory.objects.filter(author=request.user).values()

    return render(request, "complaints.html", context)


def metro(request):  # easter egg
    return render(request, 'newmetro.html')


def game(request):  # easter egg
    return render(request, ["snake.html", "game2.html"][randint(0, 0)], {})


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

@login_required
def voting(request):
    if request.POST:
        current_user = int(request.user.id)
        try:
            votingvar = (request.POST['voteVariant'])
        except:
            return render(request, "voting.html")

        votingid = (request.GET.get('id'))
        dbcoonnect = models.VotingsBase.objects.filter(id=votingid)
        dbcoonnect1 = models.VotingsBase.objects.get(id=votingid)
        dblist=dbcoonnect.values_list()
        counter=-1
        t=models.VotingsBase.objects.get(id=votingid)

        ss = models.VotingHistory.objects.filter(golosid=votingid).filter(userid=int(current_user))

        if not ss.exists():

            try:
                if dblist[0][4]==votingvar:
                    s = models.VotingHistory(golosid=int(votingid), userid=int(current_user))
                    s.save()
                    t.option1counter += 1
                    t.save()
            except:
                pass
            try:
                if dblist[0][6]==votingvar:
                    s = models.VotingHistory(golosid=int(votingid), userid=int(current_user))
                    s.save()
                    t.option2counter += 1
                    t.save()
            except:
                pass

            try:
                if dblist[0][8]==votingvar:
                    s = models.VotingHistory(golosid=int(votingid), userid=int(current_user))
                    s.save()
                    t.option3counter += 1
                    t.save()
            except:
                pass

            try:
                if dblist[0][10]==votingvar:
                    s = models.VotingHistory(golosid=int(votingid), userid=int(current_user))
                    s.save()
                    t.option4counter += 1
                    t.save()
            except:
                pass


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
                i.append(0)
        return render(request, "voting.html", res)
    return render(request, "voting.html")


def logout_func(request):
    logout(request)
    return redirect('/')