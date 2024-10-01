from django.contrib import admin

# Register your models here.
from .models import UserDB
admin.site.register(UserDB)


# class UserDBAdmin(admin.ModelAdmin):
# list_display = ('user_id','sellername','phone_no','role','created_at','status')
#
# admin.site.register(UserDB, UserDBAdmin)
