from .models import Mymodelresults, Moviereview


def get_all_Mymodelresults_objects():
    # returns a query set of all modelresults objects
    return Mymodelresults.objects.all()

def get_movie_names():
    movies = Mymodelresults.objects.values_list('movie', flat=True).distinct()
    return list(movies)


