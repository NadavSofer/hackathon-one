from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class profile_view(generic.DetailView):
    model = User
    template_name= 'profile.html'
    context_object_name = 'profile'

class signup_view(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'