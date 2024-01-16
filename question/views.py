from .serializers import *
from .models import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login, logout

class QuestionAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, question_id):
        raw_questions = Question.objects.order_by('?').filter(pk=question_id)[:10]
        serializer = QuestionSerializer(raw_questions, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class UserScoreList(APIView):
    def post(self, request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
            user_score = request.data.get('score') 

            if user_score not in [0, 5]:
                return Response({"error": "Invalid score. Score must be either 0 or 5."}, status=status.HTTP_400_BAD_REQUEST)

            # Update the user's score based on the provided score
            user = request.user  # Assuming the user is authenticated
            user_score_instance, created = UserScore.objects.get_or_create(user=user)
            
            user_score_instance.score += user_score
            user_score_instance.save()

            return Response({"score": user_score_instance.score}, status=status.HTTP_200_OK)
        
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
  
class Leaderboard(APIView):
    def get(self, request):
        top_users = UserScore.objects.order_by('-score')[:10]
        serializer = UserScoreSerializer(top_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)