from django.db import models

# Create your models here.
class TestScore(models.Model):
    first_round = models.IntegerField()
    second_round = models.IntegerField()
    third_round = models.IntegerField()

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    test_score = models.OneToOneField(TestScore, on_delete=models.CASCADE)