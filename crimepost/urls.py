from django.urls import path, include
from crimepost.views import Crime, CrimeView, SaveNews, ReadLaters, NewsCategory1
app_name = "crimepost"
urlpatterns = [
    path("", Crime, name="crimeall"),
    path("CrimeView/<str:title>/<str:headline>/<int:pk>/", CrimeView, name="crimeview"),
    path("NewsCate/<int:pk>/", NewsCategory1, name="crimecate"),
    path("SaveNews", SaveNews, name="savenews" ),
    path("Save_For_Later", ReadLaters, name="read"),
    #path("Join_NewsLetter", NewsLetters, name="newsletter"),
]