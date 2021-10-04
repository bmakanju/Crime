from django.urls import path, include
from fashion.views import Fashions, FashionView, SaveFashion, ReadLater, FashionComment, FashionCommentAll #SeplyView, FashionReply
app_name = "fashion"
urlpatterns = [
    path("Fashion_News", Fashions.as_view(), name="fashionnews"),
    path("FashionComment",FashionComment, name="fashioncomment"),
   # path("FashionReply",FashionReply, name="fashionreply"),
    path("FashionCommentAll/<int:pk>", FashionCommentAll, name="fashioncommentall"),
    #path("FashionViewReply/<int:pk>", SeplyView, name="seplyview"),
    path("FashionView/<str:title>/<str:headline>/<int:pk>/", FashionView, name="fashionview"),
]