from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .views import login_view, ProfilesList, ProfileDetail

app_name = "profiles"

urlpatterns = [
    path(
        "login/",
        login_view,
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("profiles:profiles_list")),
        name="logout",
    ),
    path("profiles/", ProfilesList.as_view(), name='profiles_list'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail')
]