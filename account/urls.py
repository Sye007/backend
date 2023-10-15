from django.urls import path
from .views import signup, login
#from .views import login


urlpatterns = [
    path("signup/", signup),
    path("login/", login),
]