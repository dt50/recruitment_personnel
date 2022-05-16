from django.urls import path
from django.urls import reverse_lazy
from .views import TableView, promotion_position

app_name = "departments"

urlpatterns = [
    path("table/", TableView.as_view(), name="table"),
    path("table/ws/<int:pk>/", promotion_position, name="promotion"),
]
