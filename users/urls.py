from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.ProfileSelf.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("token-login", obtain_auth_token),
    path("jwt-login", views.JWTLogIn.as_view()),
    path("github", views.GithubLogin.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
