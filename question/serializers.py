from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('id','question','answer', 'options')
    def get_options(self, obj):
        return [obj.option_one, obj.option_two, obj.option_three, obj.option_four]


class UserScoreSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    # time_taken = serializers.SerializerMethodField()
    class Meta:
        model = UserScore
        fields = ('username', 'score', 'time_taken')

    # def get_time_taken(self, obj):
    #     total_seconds = obj.time_taken
    #     minutes = int(total_seconds // 60)
    #     seconds = int(total_seconds % 60)
    #     return f"{minutes:02d}:{seconds:02d}"
    

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    time_taken = serializers.SerializerMethodField()
    class Meta:
        model = UserScore
        fields = ['username', 'score', 'time_taken']

    def get_time_taken(self, obj):
        total_seconds = obj.time_taken
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"