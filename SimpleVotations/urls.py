from django.contrib import admin
from django.urls import path


from votation import auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", auth_viewsviews.login_page),
    path("singup/", auth_views.singup_page)

]
