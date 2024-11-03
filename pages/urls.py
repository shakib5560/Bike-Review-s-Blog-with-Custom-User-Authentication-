
from django.urls import path, include
from .views import home, blog, createpost, updatepost, deletepost, register


urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("createpost/", createpost, name="createpost"),
    path("deletepost/<int:pk>/", deletepost, name="deletepost"),
    path("updatepost/<int:pk>/", updatepost, name="updatepost"),
    path("register/", register, name="register" ),
]