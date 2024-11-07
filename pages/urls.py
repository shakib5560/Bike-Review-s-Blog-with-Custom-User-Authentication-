
from django.urls import path, include
from .views import home, blog, createpost, updatepost, deletepost, register, profiles, logout_view, change_password, logout_view


urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("createpost/", createpost, name="createpost"),
    path("deletepost/<int:pk>/", deletepost, name="deletepost"),
    path("updatepost/<int:pk>/", updatepost, name="updatepost"),
    path("register/", register, name="register" ),
    path("accounts/profile/", profiles, name="profile",),
    path("logout/", logout_view, name="logout"),
    path("accounts/password-change", change_password, name='modyfypassword'),
    path("accounts/logout_view", logout_view, name="logout_view"),
]