from urllib.parse import urlparse

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect

from votation.forms import RegistrationForm


def check_redirection_url_safety(request, url):
    parsed = urlparse(url)
    current_site = get_current_site(request)
    if not parsed.netloc or parsed.netloc == current_site.domain:
        return True
    return False


def login_page(request):
    context = dict()
    next_page = request.GET.get('next', '/')
    if not check_redirection_url_safety(request, next_page):
        next_page = '/'
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(next_page)
    return render(request, 'login.html', context)


def signup_page(request):
    next_page = request.GET.get('next', '/login')
    if not check_redirection_url_safety(request, next_page):
        next_page = '/login'
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
                password=form.data.get('password'),
            )
            user.save()
            login(request, user)
            return redirect(next_page)
        else:
            context['form'] = form

    return render(request, 'signin.html', context)
