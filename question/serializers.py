from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('question','image_url', 'answer', 'options')
    def get_options(self, obj):
        return [obj.option_one, obj.option_two, obj.option_three, obj.option_four]



#Score 

class UserScoreSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserScore
        fields = ('user', 'score')
# class UserScoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserScore
#         fields = 