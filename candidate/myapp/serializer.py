from rest_framework.serializers import ModelSerializer
from .models import Candidate, TestScore


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        # depth = 1


class TestScoreSerializer(ModelSerializer):
    class Meta:
        model = TestScore
        fields = '__all__'
        # depth = 1


class AverageScoreSerializer(ModelSerializer):
    class Meta:
        model = TestScore
        fields = '__all__'
        # depth = [