from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.views.generic import ListView

from .forms import RegistrationForm, LoginForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        check = request.POST.get("check-reg", None)

        if form.is_valid() and (check == "true"):
            form.save()
            login(
                request,
                user=authenticate(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password1"],
                ),
            )
            return redirect("quizes:main-view")
        else:
            error_text = "<ul>"

            for msg_list in form.errors.values():
                for msg in msg_list:
                    error_text += f"<li>{msg}</li>"
            if check != "true":
                error_text += "<li>Вы не подтвердили согласие на регистрацию</li>"
            error_text += "</ul>"

            messages.error(request, mark_safe(error_text))

    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "users/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user=user)
                    return redirect(reverse_lazy("quizes:main-view"))
            else:
                error_text = "<ul><li>Неправильный логин или пароль</li></ul>"
                messages.error(request, mark_safe(error_text))
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "users/login.html", context)


class Profiles(ListView):
    model = Profile
    template_name = "profiles/profiles.html"
    context_object_name = "profile_list"
    paginate_by = 12
