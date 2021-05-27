from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, TestScoreViewSet, AverageScore
    # AverageScoreViewSet
from django.urls import include, path
router = DefaultRouter()
router.register(r'candidate', CandidateViewSet)
router.register(r'testscore', TestScoreViewSet)
# router.register(r'Averagescore', AverageScore)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]