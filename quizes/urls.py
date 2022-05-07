from django.urls import path
from .views import QuizListView, quiz_view, quiz_data_view, save_quiz_view, HomePageView

app_name = "quizes"

urlpatterns = [
    path("", HomePageView.as_view(), name="main-view"),
    path("list/", QuizListView.as_view(), name="quiz-list"),
    path("list/<pk>/", quiz_view, name="quiz-view"),
    path("list/<pk>/save/", save_quiz_view, name="save-view"),
    path("list/<pk>/data/", quiz_data_view, name="quiz-data-view"),
]
