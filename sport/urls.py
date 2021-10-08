from django.urls import path, include
from sport.views import Sports, SportView, SaveSport, ReadLater, SportCategory1, SportComment, SportCommentAll, SeplyView, SportReply
app_name = "sport"
urlpatterns = [
    path("Sport_News", Sports, name="sportnews"),
    path("SportCate/<int:pk>/", SportCategory1, name="sportcate"),
    path("SportComment",SportComment, name="sportcomment"),
    path("SportReply",SportReply, name="sportreply"),
    path("SportCommentAll/<int:pk>", SportCommentAll, name="sportcommentall"),
    path("SportViewReply/<int:pk>", SeplyView, name="seplyview"),
    path("SportView/<str:title>/<str:headline>/<int:pk>/", SportView, name="sportview"),
]