
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
def home(request):
    return render(request,'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('sentimentapi/', include('sentiment.urls',namespace='api')),
]
