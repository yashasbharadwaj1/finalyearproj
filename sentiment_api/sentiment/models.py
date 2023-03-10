# sentiment models
# sentiment_model = pipeline(model="federicopascual/finetuning-sentiment-model-3000-samples")
# my_sentiment_model = pipeline(model="yashas123/finetuning-sentiment-model")

from django.db import models
from django.http import JsonResponse


class Moviereview(models.Model):
    channelname = models.CharField(max_length=255)
    movie = models.CharField(max_length=255)
    url = models.URLField()
    hero = models.CharField(max_length=255)
    heroine = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.movie


class Mymodelresults(models.Model):
    movie = models.CharField(max_length=255)
    total_comments = models.IntegerField()
    total_positive_comments = models.IntegerField()
    total_negative_comments = models.IntegerField()
    final_verdict = models.CharField(max_length=255)

    def __str__(self):
        return self.movie

