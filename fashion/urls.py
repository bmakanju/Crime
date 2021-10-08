from django.urls import path, include
from fashion.views import Fashions, FashionView, SaveFashion, ReadLater, FashionComment, FashionCommentAll, FashionCategory1
app_name = "fashion"
urlpatterns = [
    path("Fashion_News", Fashions, name="fashionnews"),
    path("FashionCate/<int:pk>/", FashionCategory1, name="fashioncate"),
    path("FashionComment",FashionComment, name="fashioncomment"),
    #path("FashionReply",FashionReply, name="fashionreply"),
    path("FashionCommentAll/<int:pk>", FashionCommentAll, name="fashioncommentall"),
    #path("FashionViewReply/<int:pk>", FashionView, name="seplyview"),
    path("FashionView/<str:title>/<str:headline>/<int:pk>/", FashionView, name="fashionview"),
]