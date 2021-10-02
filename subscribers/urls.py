from django.urls import path, include
from subscribers.views import  NewsLetters
app_name = "subscribers"
urlpatterns = [
    path("Join_NewsLetter", NewsLetters, name="newsletter"),
]