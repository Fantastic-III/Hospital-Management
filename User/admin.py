from django.contrib import admin
from User.models import NewUser


class NewUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')


# Register your models here.
admin.site.register(NewUser, NewUserAdmin)
