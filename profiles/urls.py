from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .views import login_view, Profiles

app_name = "profiles"

urlpatterns = [

    path(
        "login/",
        login_view,
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("quizes:main-view")),
        name="logout",
    ),
    path("profiles/", Profiles.as_view()),
]
