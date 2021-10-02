from django.contrib import admin
from crimepost.models import Like, Dislike, Love, Comment, Reply, News, Views, ReadLater
# Register your models here.
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Love)
admin.site.register(Views)
admin.site.register(ReadLater)

#admin.site.register()
