from django.urls import path, include
from entertain.views import Entertains, EntertainView, SaveEntertain, ReadLater, EntertainComment, EntertainCommentAll, EntertainCategory1
app_name = "entertain"
urlpatterns = [
    path("Entertain_News", Entertains, name="entertainnews"),
    path("EntertainCate/<int:pk>/", EntertainCategory1, name="entertaincate"),
    path("EntertainComment",EntertainComment, name="entertaincomment"),
    #path("EntertainReply",EntertainReply, name="entertainreply"),
    path("EntertainCommentAll/<int:pk>", EntertainCommentAll, name="entertaincommentall"),
    #path("EntertainViewReply/<int:pk>", EntertainView, name="seplyview"),
    path("EntertainView/<str:title>/<str:headline>/<int:pk>/", EntertainView, name="entertainview"),
]