from django.contrib import admin
from django.urls import path

from first import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index_page),
    path("login/", views.login_page)
]
