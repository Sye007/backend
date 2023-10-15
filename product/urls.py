from django.urls import path
from .views import hello
from .views import createfood

urlpatterns = [
    path("allfood/", hello),

    path("create/", createfood)
]