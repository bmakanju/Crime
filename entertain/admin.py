from django.contrib import admin
from entertain.models import Eomment, Entertain, ReadLaterEntertain, EntertainCate
# Register your models here.
class EntertainA(admin.ModelAdmin):
    #search_by = ["title"]
    list_display = ("title","headline","pk",)
    #search_by = ("title", "headline")
admin.site.register(Entertain, EntertainA)
admin.site.register(Eomment)
admin.site.register(EntertainCate)

admin.site.register(ReadLaterEntertain)

#admin.site.register()
