from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from customers.models import PurchaseHistory
from django.contrib.auth.models import User


# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class EditProfile(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name']
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')


class UserLogin(LoginView):
    template_name = 'login.html'


def profile(request):
    current_user = request.user
    user_history = PurchaseHistory.objects.filter(user=current_user)
    return render(request, 'profile.html', {'history': user_history})


def user_logout(request):
    logout(request)
    return redirect('home')
