from django.contrib import admin
from django.urls import path


from votation import auth_views, views, votingEngine

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", auth_views.login_page),
    path("signup/", auth_views.signup_page),
    path("", views.main)

]
