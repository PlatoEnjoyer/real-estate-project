from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm


# Create your views here.
def registration(request):
    err = ""

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            err = form.errors

    print(err)

    form = RegisterForm()
    return render(request, "registration/register.html", {"form": form, "error": err})


class LoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
