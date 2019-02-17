from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from votation import auth_views, views, votingEngine

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", auth_views.login_page),
    path("signup/", auth_views.signup_page),
    path("", views.main),
    path("profile/", views.profile),
    path("complaints/", views.complain),
    path("dbadd", votingEngine.testing),
    path('game/', views.game),
    path("new_vote/", views.new_vote),
    path("new_metro/", views.metro),
    path("voting/", views.voting),
    path("logout/", views.logout_func),
    path("complaint/",  views.view_complaint),
    path("about/", views.about())
]

urlpatterns += staticfiles_urlpatterns()
