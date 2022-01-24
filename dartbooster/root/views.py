from django.shortcuts import render
from user.views import LoginView
# Create your views here.

class HomeView(LoginView):
    template_name= __package__+'/home.html'
