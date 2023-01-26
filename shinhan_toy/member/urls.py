from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.MemberRegisterView.as_view()),
    path("/password", views.ChangePasswordView.as_view()),
]