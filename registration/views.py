from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, views
from django.urls import reverse


def login(request):
    template_response = views.login(request)
    return template_response
