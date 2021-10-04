from django.urls import path, include
from beauty.views import Beautys, BeautyView, SaveBeauty, ReadLater, BeautyComment, BeautyCommentAll
app_name = "beauty"
urlpatterns = [
    path("Beauty_News", Beautys.as_view(), name="beautynews"),
    path("BeautyComment",BeautyComment, name="beautycomment"),
    #path("BeautyReply",BeautyReply, name="beautyreply"),
    path("BeautyCommentAll/<int:pk>", BeautyCommentAll, name="beautycommentall"),
   # path("BeautyViewReply/<int:pk>", BeplyView, name="beautyview"),
    path("BeautyView/<str:title>/<str:headline>/<int:pk>/", BeautyView, name="beautyview"),
]