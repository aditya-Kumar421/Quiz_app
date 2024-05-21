from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError

from .serializers import *
from .models import *

class QuestionGETView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:
            raw_questions = Question.objects.order_by("?").filter(pk=id)[:10]
        except Question.DoesNotExist:
            return Response({"Question not found"})
        serializer = QuestionSerializer(raw_questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionUpdateDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        try:
            qus = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"Question not found"})
        serializer = QuestionSerializer(qus, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg: Question Updated successfully!"})
        return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            qus = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"Question not found"})
        qus.delete()
        return Response({"Question deleted successfully!"})

class QuestionPOSTView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"msg: Question added successfully!"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)

    def get(self, request):
        all_Questions = Question.objects.all()
        serializer = QuestionSerializer(all_Questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserScoreList(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            score = request.data.get("score")
            time_left = request.data.get("time_taken")
            time_taken = 2700 - time_left
            if score is None or time_taken is None:
                raise ValidationError("Score and time_taken are required.")
            
            if not isinstance(score, int) or not isinstance(time_taken, int):
                raise ValidationError("Score and time_taken must be integers.")
            
            if score < 0 or time_taken < 0:
                raise ValidationError("Score and time_taken must be non-negative.")

            user_score, created = UserScore.objects.get_or_create(user=request.user)

            user_score.score = score
            user_score.time_taken = time_taken
            user_score.save()

            return Response(
                {"msg": "Answers submitted successfully!"},
                status=status.HTTP_200_OK
            )

        except ValidationError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)

class ViewScore(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user_score = UserScore.objects.filter(user=request.user)
            serializer = UserScoreSerializer(user_score)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            raise APIException(str(e))
        
class Leaderboard(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        users = UserScore.objects.all()
        sorted_users = sorted(users, key=lambda x: (-x.score, x.time_taken))
        serializer = LeaderboardSerializer(sorted_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    