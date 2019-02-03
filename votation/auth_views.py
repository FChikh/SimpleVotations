from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import NoReverseMatch

from votation.forms import RegistrationForm, LoginForm


def login_page(request):
    context = dict()
    next_page = request.GET.get('next', '/')
    username = password = ''
    context['next'] = next_page
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    return redirect(next_page)
                except NoReverseMatch:
                    return redirect('/')
            else:
                form = LoginForm()
                messages.error(request, 'Пользователь неактивен')
                context['form'] = form
                return render(request, 'login.html', context)
        else:
            form = LoginForm()
            messages.error(request, 'Неверные логин или пароль')
            context['form'] = form
            return render(request, 'login.html', context)
    return render(request, 'login.html', context)


def signup_page(request):
    next_page = request.GET.get('next', '/login')
    context = dict()
    context['title'] = 'Регистрация'

    if request.method == "GET":
        context['form'] = RegistrationForm()
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.data.get('username'),
                    email=form.data.get('email'),
                    password=form.data.get('password'),
                )
            except IntegrityError:
                messages.error(request, 'Пользователь с таким логином уже существует')
                return render(request, 'signin.html', context)
            else:
                user.save()
                login(request, user)
                try:
                    return redirect(next_page)
                except NoReverseMatch:
                    return redirect('/')
        else:
            context['form'] = form

    return render(request, 'signin.html', context)
