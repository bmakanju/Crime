from django.contrib import admin
from sport.models import Like, Dislike, Love, Somment, Seply, Sport, Views, ReadLaterSport
# Register your models here.
admin.site.register(Sport)
admin.site.register(Somment)
admin.site.register(Seply)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Love)
admin.site.register(Views)
admin.site.register(ReadLaterSport)

#admin.site.register()
