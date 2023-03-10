app_name = "sentiment"
from django.urls import path
from .views import *

urlpatterns = [
    #GET
    path('getallverdicts/', list_allmovie_verdicts, name='allverdicts'),

    #GET and POST
    path('filtersentimentbymovie/',filter_verdict_by_movie,name='movie_filter')

]
