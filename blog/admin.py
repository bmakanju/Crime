from django.contrib import admin
from blog.models import Comment, Blog, ReadLaterBlog
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
#admin.site.register(Seply)
#admin.site.register(Like)
#admin.site.register(Dislike)
#admin.site.register(Love)
#.site.register(Views)
admin.site.register(ReadLaterBlog)

#admin.site.register()
