from django.contrib import admin
from account.models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'fname', 'lname', 'profilepic','bio','pk']
admin.site.register(Profile, ProfileAdmin)