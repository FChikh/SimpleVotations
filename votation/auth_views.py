from urllib.parse import urlparse

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from votation.forms import RegistrationForm


def check_redirection_url_safety(request, url):
    parsed = urlparse(url)
    current_site = get_current_site(request)
    if not parsed.netloc or parsed.netloc == current_site.domain:
        return True
    return False


def registration_page(request):
    next_page = request.GET.get('next', '/')
    if not check_redirection_url_safety(request, next_page):
        next_page = '/'
    if request.user.is_authenticated:
        return redirect(next_page)
    context = dict()
    context['title'] = 'Регистрация'
    if request.method == "GET":
        context['form'] = RegistrationForm()
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.data.get('username'),
                email=form.data.get('email'),
                password=form.data.get('password_first'),
            )
            user.save()
            login(request, user)
            return redirect(next_page)
        else:
            context['form'] = form
    return render(request, 'registration.html', context)