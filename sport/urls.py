from django.urls import path, include
from sport.views import Sports, SportView, SaveSport, ReadLater, SportComment, SportCommentAll, SeplyView, SportReply
app_name = "sport"
urlpatterns = [
    path("Sport_News", Sports.as_view(), name="sportnews"),
    path("SportComment",SportComment, name="sportcomment"),
    path("SportReply",SportReply, name="sportreply"),
    path("SportCommentAll/<int:pk>", SportCommentAll, name="sportcommentall"),
    path("SportViewReply/<int:pk>", SeplyView, name="seplyview"),
    path("SportView/<str:title>/<str:headline>/<int:pk>/", SportView, name="sportview"),
]