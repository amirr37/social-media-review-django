from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from Post.models import Post

from Account.forms import UserRegistrationForm, UserLoginForm, ResetPasswordForm


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'Account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('Home:index-page')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created for ' + form.cleaned_data['username'])
            return redirect('Home:index-page')
        return render(request, self.template_name, {'form': form, })


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'Account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home:index-page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in')
                return redirect('Home:index-page')
            messages.error(request, 'Invalid username or password')

        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'You have been logged out')
            return redirect('Account:register')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        # user = User.objects.get(pk=id)
        user = get_object_or_404(User, pk=id)

        posts = Post.objects.filter(author=user, is_active=True)
        return render(request, 'Account/profile.html', {'user': user, 'posts': posts})


class UserPasswordResetView(PasswordResetView):
    template_name = 'Account/reset_password.html'
    success_url = reverse_lazy('Account:reset-password-done')
    email_template_name = 'Account/reset_password_email.html'



class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'Account/reset_password_done.html'
