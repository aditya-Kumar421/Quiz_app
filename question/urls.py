from django.urls import path
from .views import *
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('question/<int:id>/', QuestionGETView.as_view()),
    path('change/<int:pk>/', QuestionUpdateDeleteView.as_view()),
    path('questions/', QuestionPOSTView.as_view()),
    path('score/<int:question_id>/', UserScoreList.as_view(), name='user-scores'),
    path('leaderboard/', Leaderboard.as_view(), name='leaderboard'),
]