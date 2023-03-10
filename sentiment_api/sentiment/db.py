from .models import Mymodelresults, Moviereview


def get_all_Mymodelresults_objects():
    # returns a query set of all modelresults objects
    return Mymodelresults.objects.all()



