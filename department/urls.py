from django.urls import path
from django.urls import reverse_lazy
from .views import table_view

app_name = "departments"

urlpatterns = [
    path('table/', table_view)
]
