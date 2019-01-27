from django.contrib import admin
from django.urls import path

from votation import views
from votation import votingEngine

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login_page),
    path("singup/", views.singup_page),
]
