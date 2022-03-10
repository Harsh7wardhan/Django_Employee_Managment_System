# from django.conf.urls import url
# from django.urls import re_path as url
from django.urls import include, path
from django.conf.urls import include
from . import views
from django.urls import re_path as url


app_name = "accounts"

urlpatterns = [
    url(r"^register/$", views.register, name = "signup"),
    url(r"^login/$", views.sign_in, name = "signin"),
    url(r"^logout/$", views.logout_view, name = "logout"),
]
