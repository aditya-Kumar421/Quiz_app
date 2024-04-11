from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('id','question','image_url', 'answer', 'options')
    def get_options(self, obj):
        return [obj.option_one, obj.option_two, obj.option_three, obj.option_four]


class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ('user', 'score')

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserScore
        fields = ['username', 'score']