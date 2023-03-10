from .models import Moviereview, Mymodelresults
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviereview
        fields = "__all__"


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mymodelresults
        fields = "__all__"
