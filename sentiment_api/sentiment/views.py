from .serializers import ResultsSerializer, ReviewSerializer

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from rest_framework.parsers import JSONParser
from rest_framework import status
from .db import *
from rest_framework.response import Response
from .forms import *
from rest_framework.decorators import api_view
import json
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64


@api_view(["GET"])
def list_allmovie_verdicts(request):
    if request.method == 'GET':
        allobjs = get_all_Mymodelresults_objects()
        serialized = ResultsSerializer(data=allobjs, many=True)
        if not serialized.is_valid():
            ordered_dict = serialized.data
            json_str = json.dumps(ordered_dict)
            my_dict = json.loads(json_str)
            # my_dict is list of dictionaries
            """
            [{'id': 1, 'movie': 'pathan', 'total_comments': 80, 'total_positive_comments': 67, 'total_negative_comments': 13, 'final_verdict': 'positive'}, {'id': 2, 'movie': 'cirkus', '
total_comments': 739, 'total_positive_comments': 338, 'total_negative_comments': 401, 'final_verdict': 'negative'}, {'id': 3, 'movie': 'avatar the way of water', 'total_comme
nts': 321, 'total_positive_comments': 254, 'total_negative_comments': 67, 'final_verdict': 'positive'}]

            """
            # return JsonResponse(data=my_dict, safe=False)
            c = {'output':my_dict}
            return render(request, 'allverdicts.html', c)
        else:
            return JsonResponse(data={"stauts": status.HTTP_400_BAD_REQUEST})
    else:
        return JsonResponse(data={"status": "only get method allowed"})


@api_view(["GET", "POST"])
def filter_verdict_by_movie(request):
    if request.method == "GET":
        form = Verdictfilterbymovieform()
        context = {
            'form': form
        }
        return render(request, 'filterbymovie.html', context)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Verdictfilterbymovieform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            movie_choice = form.cleaned_data['moviechoice']
            # print(movie_choice)
            particular_obj = Mymodelresults.objects.get(movie=movie_choice)
            # print(type(particular_obj))<class 'sentiment.models.Mymodelresults'>

            # print(particular_obj.total_comments)
            mylabels = ["positive_comments", "negtive_comments"]
            myvalues = [particular_obj.total_positive_comments, particular_obj.total_negative_comments]
            fig, ax = plt.subplots(figsize=(7, 7))
            ax.pie(myvalues, labels=mylabels)
            ax.legend(myvalues, title="Number of Comments", loc="center")
            ax.set_title('Comments Distribution')

            # Save the chart as a PNG image in memory
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)

            # Encode the PNG image as a base64 string
            b64image = base64.b64encode(buffer.getvalue()).decode()
            d = {
                'image': b64image,
                'movie': particular_obj.movie,
                'allcomments': particular_obj.total_comments,
                'verdict': particular_obj.final_verdict
            }

            return render(request, 'filterbymovie.html', d)
