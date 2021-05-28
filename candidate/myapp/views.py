from django.db.models import Avg, Max
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

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
        average = TestScore.objects.all().aggregate(Avg('first_round')), TestScore.objects.all().aggregate(
            Max('first_round')) \
            , TestScore.objects.all().aggregate(Avg('second_round')), TestScore.objects.all().aggregate(
            Max('second_round')) \
            , TestScore.objects.all().aggregate(Avg('third_round')), TestScore.objects.all().aggregate(
            Max('third_round'))

        return Response(average)


class Highest_scorer(APIView):
    def get(self, request):
        re = requests.get("http://127.0.0.1:8000/candidate/")
        max = 0
        candidate = ""
        for i in re.json():
            testscore = requests.get("http://127.0.0.1:8000/testscore/{}".format(i["test_score"])).json()
            final = testscore["first_round"] + testscore["second_round"] + testscore["third_round"]
            if final > max:
                max = final
                candidate = i["name"]
        output = {"highest Scorer": candidate}

        return Response(output)
