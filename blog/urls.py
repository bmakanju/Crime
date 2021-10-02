from django.urls import path, include
from blog.views import Blogs, BlogView, SaveBlog, ReadLater, BlogComment, BlogCommentAll, LikePost, HatePost, LovePost, DeleteComment1, DeleteComment2, EditComment
app_name = "blog"
urlpatterns = [
    path("SaveBlog", SaveBlog, name="blogsave"),
    path("LikePosT", LikePost, name="likepost"),
    path("EditComment/<int:pk>", EditComment, name="editcomment"),
    path("DeleteCommentConfirm/<int:pk>", DeleteComment1, name="deletecomment1"),
    path("DeleteComment/<int:pk>", DeleteComment2, name="deletecomment2"),
   path("LovePosT", LovePost, name="lovepost"),
       path("HatePosT", HatePost, name="hatepost"),
    path("Blog", Blogs.as_view(), name="blog"),
    path("BlogComment",BlogComment, name="blogcomment"),
    path("BlogCommentAll/<int:pk>", BlogCommentAll, name="blogcommentall"),
   path("BlogView/<str:title>/<str:headline>/<int:pk>/", BlogView, name="blogview"),
   path("Save_Blog_Post_For_Later", ReadLater, name="blogpostsave"),
]