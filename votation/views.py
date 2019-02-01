from django.contrib import messages
from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import render
<<<<<<< Updated upstream
=======
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from votation import votingEngine
from votation.forms import ProfileEditForm
>>>>>>> Stashed changes


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
    data = dict()
    data = (votingEngine.friendly_extract_for_profile(1))
    data['name'] = request.user.username
    data['surname'] = request.user.email
    print(data)

    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            try:
                user_old = User.objects.get(username=data['name'])
                new_username = form.data.get('username') if not None else user_old.username
                new_email = form.data.get('email') if None else user_old.email
                print(new_username, new_email)
                if form.data.get('password') is None:
                    user = User.objects.filter(username=data['name']).update(
                        username=new_username,
                        email=new_email,
                    )
                else:
                    user = User.objects.filter(username=data['name']).update(
                        username=new_username,
                        email=new_email,
                        password=form.data.get('password'),
                    )
                    login(new_username, form.data.get('password'))

            except IntegrityError:
                messages.error(request, 'Пользователь с таким логином уже существует')
                return render(request, 'profile.html', data)
        else:
            return render(request, 'profile.html', data)
    return render(request, "profile.html", data)
