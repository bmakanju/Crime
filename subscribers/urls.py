from django.urls import path, include
from subscribers.views import  NewsLetters, Unsub1, Unsub2
app_name = "subscribers"
urlpatterns = [
    path("Join_NewsLetter", NewsLetters, name="newsletter"),
    path("Unsubscribe_From_Newsletter", Unsub1, name="unsub1"),
    path("Unsubscribing_From_CrimeHeist_Newsletter/<int:pk>/", Unsub2, name="unsub2"),
]