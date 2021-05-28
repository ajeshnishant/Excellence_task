from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, TestScoreViewSet, AverageScore , Highest_scorer
from django.urls import include, path
router = DefaultRouter()
router.register(r'candidate', CandidateViewSet)
router.register(r'testscore', TestScoreViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('average', AverageScore.as_view(),name='average'),
    path('highest', Highest_scorer.as_view(),name='highest'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
