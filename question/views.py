from .serializers import *
from .models import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class QuestionGETView(APIView):
    permission_classes = [IsAuthenticated]
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

    def post(self, request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
            user_score = request.data.get("score")

            if user_score not in [0, 5]:
                return Response(
                    {"error": "Invalid score. Score must be either 0 or 5."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user_score_instance, created = UserScore.objects.get_or_create(
                user=request.user
            )

            user_score_instance.score += user_score
            user_score_instance.save()

            return Response(
                {"score": user_score_instance.score}, status=status.HTTP_200_OK
            )

        except Question.DoesNotExist:
            return Response(
                {"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND
            )


class Leaderboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        top_users = UserScore.objects.order_by("-score")[:10]
        serializer = UserScoreSerializer(top_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
