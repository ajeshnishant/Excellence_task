from django.shortcuts import render

# Create your views here.
from django.db.models import Avg , Max
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import CandidateSerializer, TestScoreSerializer
from .models import Candidate, TestScore
# Create your views here.



class CandidateViewSet(ModelViewSet):

    queryset = Candidate.objects.all().order_by('id')
    serializer_class = CandidateSerializer


class TestScoreViewSet(ModelViewSet):

    queryset = TestScore.objects.all().order_by('id')
    serializer_class = TestScoreSerializer


class AverageScore(APIView):
    def get(self, request):
        average = TestScore.objects.all().aggregate(Avg('first_round')),TestScore.objects.all().aggregate(Max('first_round'))\
        ,TestScore.objects.all().aggregate(Avg('second_round')),TestScore.objects.all().aggregate(Max('second_round'))\
            ,TestScore.objects.all().aggregate(Avg('third_round')), TestScore.objects.all().aggregate(Max('third_round'))

        return Response(average)