from django import forms
from .db import *


class Verdictfilterbymovieform(forms.Form):
    querysetobjects = get_all_Mymodelresults_objects()
    li = []
    for obj in querysetobjects:
        li.append(obj.movie)
    choices = tuple((name, f"{name}=>{i+1}") for i, name in enumerate(li))
    #print(choices)
    #(('pathan', 'pathan=>1'), ('cirkus', 'cirkus=>2'), ('avatar the way of water', 'avatar the way of water=>3'))

    moviechoice = forms.ChoiceField(choices=choices)
