app_name = "sentiment"
from django.urls import path
from .views import *

urlpatterns = [

    #GET
    path('getallverdicts/', list_allmovie_verdicts, name='allverdicts'),

    #GET
    path('getallmovienames/',allmovienames,name='allmovienamesindb'),
    #GET and POST
    path('filtersentimentbymovie/<str:name>/',filter_verdict_by_movie,name='movie_filter')

]
