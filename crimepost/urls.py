from django.urls import path, include
from crimepost.views import Crime, CrimeView, SaveNews, ReadLaters
app_name = "crimepost"
urlpatterns = [
    path("", Crime.as_view(), name="crimeall"),
    path("CrimeView/<str:title>/<str:headline>/<int:pk>/", CrimeView, name="crimeview"),
    path("SaveNews", SaveNews, name="savenews" ),
    path("Save_For_Later", ReadLaters, name="read"),
    #path("Join_NewsLetter", NewsLetters, name="newsletter"),
]