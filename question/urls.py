from django.urls import path
from .views import *

urlpatterns = [
    path('question/<int:id>/', QuestionGETView.as_view()),
    path('change/<int:pk>/', QuestionUpdateDeleteView.as_view()),
    path('questions/', QuestionPOSTView.as_view()),
    path('score/', UserScoreList.as_view(), name='user-scores'),
    path('leaderboard/', Leaderboard.as_view(), name='leaderboard'),
]